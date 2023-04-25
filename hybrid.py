import data as data
import numpy as np
from scipy.spatial.distance import pdist, squareform

def HierarchicalHub(dataset):
    # Add the first set of clusters, every data point is a cluster
    Clustertree = data.ClusterTree()
    Clustertree.clusters = np.array([dataset])

    # Calculate the distance matrix
    distance = CalculateDistance(Clustertree.clusters[0])

    cluster_history = [Clustertree.clusters] # list to store the clusters at each iteration

            # Find the indices of the two closest clusters
    min_row_idx, min_col_idx = FindMinDistance(distance)
    print(f"The two clusters with the smallest distance are {min_row_idx} and {min_col_idx}")

        # Merge the two closest clusters
    newcluster = MergeClosestCluster(min_row_idx, min_col_idx, Clustertree.clusters[0])

    while(len(newcluster.cluster) >= 2):
        # Find the indices of the two closest clusters
        min_row_idx, min_col_idx = FindMinDistance(distance)
        print(f"The two clusters with the smallest distance are {min_row_idx} and {min_col_idx}")

        # Merge the two closest clusters
        newcluster = MergeClosestCluster(min_row_idx, min_col_idx, newcluster)
        Clustertree.clusters = np.concatenate((Clustertree.clusters, [newcluster]))


        # Remove the two clusters that were just merged and add the new cluster
        distance = np.delete(distance, [min_row_idx, min_col_idx], axis=0)
        distance = np.delete(distance, [min_row_idx, min_col_idx], axis=1)
        newdistances = CalculateDistance(newcluster)
        distance = newdistances;

        cluster_history.append(newcluster) # append the current set of clusters to the history

    Clustertree.cluster_history = cluster_history # add the cluster history to the ClusterTree object

    return Clustertree


def CalculateDistance(clusters):
    centroids = np.array([c.centroid.values for c in clusters.cluster]) # get the centroids of all clusters
    distance = pdist(centroids) # compute pairwise distances between centroids
    
    # Convert the condensed distance matrix to a square distance matrix
    distance = squareform(distance, force='nochecks')
    
    # Set the diagonal elements to infinity to exclude comparisons with itself
    np.fill_diagonal(distance, np.inf) 
    
    return distance


def FindMinDistance(distance):
    # Get the flattened upper triangle of the distance matrix
    flattened_dist = distance[np.triu_indices(distance.shape[0], k=1)] 
    # Get the index of the minimum distance in the flattened array
    min_dist_idx = np.argmin(flattened_dist) 
    # Convert the flattened index to the row and column indices in the distance matrix
    min_row_idx, min_col_idx = np.unravel_index(min_dist_idx, (distance.shape[0], distance.shape[0])) 
    return min_row_idx, min_col_idx


def MergeClosestCluster(min_row_idx, min_col_idx, clusters):
    newcluster = data.Cluster()
    newcentroid = np.mean([clusters.cluster[min_row_idx].centroid.values, clusters.cluster[min_col_idx].centroid.values], axis=0)
    data1 = data.DataPoint()
    data1.values = newcentroid
    newcluster.centroid = data1
    newcluster.cluster_id = clusters.cluster[min_row_idx].cluster_id
    newcluster.values = np.concatenate((clusters.cluster[min_row_idx].values, clusters.cluster[min_col_idx].centroid.values))
    
    # Create new clusters object with all clusters except the two being merged
    newclusters = data.Clusters()
    newclusters.cluster = np.delete(clusters.cluster, [min_row_idx, min_col_idx])
    newclusters.cluster = np.concatenate((newclusters.cluster, [newcluster,]))

    
    return newclusters
