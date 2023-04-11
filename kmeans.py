import numpy as np
import random
import data as d

#generate random centroids for the first pass 
def GenerateRandomCentroid(dataset, kvalue):
    clusters = d.Clusters()
    temparray = np.array([])

    for k in range(kvalue):
        cluster = d.Cluster()
        randomselection = random.choice(dataset.data)
        cluster.cluster_id = k
        cluster.centroid = randomselection
        cluster.centroid.cluster_id = k
        temparray = np.append(temparray, cluster)


    clusters.cluster = np.array(temparray)
    
    return clusters

def Cluster(dataset, centroid):

    for e in dataset.data:
        distance = []
        for i in centroid.cluster: 
            distance = np.append(distance, np.linalg.norm(i.centroid.values - e.values))
        e.cluster_id = distance.tolist().index(min(distance))


    return dataset
            
        