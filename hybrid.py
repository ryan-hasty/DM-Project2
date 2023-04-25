import data as data
import numpy as np
from scipy.spatial.distance import pdist, squareform

def HierarchicalHub(dataset):
    #Add the first set of clusters, every data point is a cluster
    Clustertree = data.ClusterTree()
    Clustertree.clusters = np.array([dataset])
    #Find the min of the first two closest clusters, and combine them
    min_row_idx, min_col_idx = CalculateDistance(dataset)
    newclusters = MergeClosestCluster(min_row_idx, min_col_idx, dataset)
    Clustertree.clusters = np.append(Clustertree.clusters, newclusters)

    while(len(newclusters.cluster) > 1):
        min_row_idx, min_col_idx = CalculateDistance(newclusters)
        newclusters = MergeClosestCluster(min_row_idx, min_col_idx, newclusters)
        Clustertree.clusters = np.append(Clustertree.clusters, newclusters)

    return Clustertree



def CalculateDistance(clusters):
    centroids = []
    for i in clusters.cluster:
        centroids.append(i.centroid.values)
    
    distance = pdist(centroids) # compute pairwise distances between centroids
    
    # Convert the condensed distance matrix to a square distance matrix
    distance = squareform(distance, force='nochecks')
    
    # Set the diagonal elements to infinity to exclude comparisons with itself
    np.fill_diagonal(distance, np.inf) 
    
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
    newcluster.cluster_id = clusters.cluster[min_row_idx].cluster_id
    newcluster.values = np.concatenate((clusters.cluster[min_row_idx].values, clusters.cluster[min_col_idx].values))
    newcluster.centroid = newdata
    
    # Create new clusters object with all clusters except the two being merged
    newclusters = data.Clusters()
    newclusters.cluster = np.delete(clusters.cluster, [min_row_idx, min_col_idx])
    newclusters.cluster = np.concatenate((newclusters.cluster, [newcluster]))

    return newclusters