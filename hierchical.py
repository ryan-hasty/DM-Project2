import data as data
import numpy as np
from scipy.spatial.distance import cdist

def HierarchicalHub(dataset):
    #Add the first set of clusters, every data point is a cluster
    Clustertree = data.ClusterTree()
    Clustertree.clusters = np.array([dataset])
    count = 0
    #Find the min of the first two closest clusters, and combine them
    min_row_idx, min_col_idx = CalculateDistance(dataset)
    newclusters = MergeClosestCluster(min_row_idx, min_col_idx, dataset)
    Clustertree.clusters = np.append(Clustertree.clusters, newclusters)

    while(count < 170):
        count += 1
        min_row_idx, min_col_idx = CalculateDistance(newclusters)
        newclusters = MergeClosestCluster(min_row_idx, min_col_idx, newclusters)
        Clustertree.clusters = np.append(Clustertree.clusters, newclusters)

    return Clustertree



def CalculateDistance(clusters):
    centroids = []
    for i in clusters.cluster:
        centroids.append(i.centroid)

    num_centroids = len(centroids)
    distance = np.zeros((num_centroids, num_centroids))

    for i in range(len(centroids)):
        for j in range(i+1, len(centroids)):
            if isinstance(centroids[j], data.DataPoint) and isinstance(centroids[i], data.DataPoint) == False:
                dist = np.linalg.norm(centroids[i] - centroids[j].values)
                centroids[j] = centroids[j].values
                distance[i, j] = dist
                distance[j, i] = dist
            elif isinstance(centroids[i], data.DataPoint) and isinstance(centroids[j], data.DataPoint) == False:
                dist = np.linalg.norm(centroids[i].values - centroids[j])
                centroids[i] = centroids[i].values
                distance[i, j] = dist
                distance[j, i] = dist
            elif isinstance(centroids[i], data.DataPoint) and isinstance(centroids[j], data.DataPoint):
                dist = np.linalg.norm(centroids[i].values - centroids[j].values)
                centroids[j] = centroids[j].values
                centroids[i] = centroids[i].values
                distance[i, j] = dist
                distance[j, i] = dist
            else:
                dist = np.linalg.norm(centroids[i] - centroids[j])
                distance[i, j] = dist
                distance[j, i] = dist
    
    min_row_idx, min_col_idx = FindMinDistance(distance)
    
    print(f"The two clusters with the smallest distance are {min_row_idx} and {min_col_idx}")
    
    clusters.amount = len(clusters.cluster)
    clusters.averagedistance = AverageDistance(distance)
    
    return min_row_idx, min_col_idx





def FindMinDistance(distance):
    # Get the flattened upper triangle of the distance matrix, excluding the diagonal
    flattened_dist = distance[np.triu_indices(distance.shape[0], k=1)]
    # Get the index of the minimum distance in the flattened array
    min_dist_idx = np.argmin(flattened_dist)
    # Convert the flattened index to the row and column indices in the distance matrix
    min_row_idx, min_col_idx = np.unravel_index(min_dist_idx, (distance.shape[0], distance.shape[0]))
    
    # If either of the clusters being compared is the same, find the next minimum distance
    if min_row_idx == min_col_idx:
        min_row_idx = 0
        min_col_idx = 1
        
    return min_row_idx, min_col_idx


def AverageDistance(distance):
    return np.mean(distance)

def MergeClosestCluster(min_row_idx, min_col_idx, clusters):
    newcluster = data.Cluster()
    newcentroid = np.mean([clusters.cluster[min_row_idx].centroid.values, clusters.cluster[min_col_idx].centroid.values], axis=0)
    newdata = data.DataPoint()
    newdata.values = newcentroid
    newcluster.cluster_id = min_row_idx * clusters.cluster.size
    if clusters.cluster[min_row_idx].centroid.candidate == False and clusters.cluster[min_row_idx].centroid.known == False: 
        newcluster.values = np.append(newcluster.values, clusters.cluster[min_row_idx].values)
        newcluster.values = np.append(newcluster.values, clusters.cluster[min_col_idx].values)
    else:
        newcluster.values = np.append(newcluster.values, clusters.cluster[min_row_idx].centroid)
        newcluster.values = np.append(newcluster.values, clusters.cluster[min_col_idx].centroid)   
           
    newcluster.centroid = newdata
    # Create new clusters object with all clusters except the two being merged
    newclusters = data.Clusters()
    newclusters.cluster = np.delete(clusters.cluster, [min_row_idx, min_col_idx])
    newclusters.cluster = np.append(newclusters.cluster, newcluster)


    return newclusters