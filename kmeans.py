import numpy as np
import random
import data as d

global THRESHOLD
THRESHOLD = 0.001
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

def Cluster(dataset, clusters):

    for e in dataset.data:
        distance = []
        for i in clusters.cluster: 
            #Euclidean
            distance = np.append(distance, np.linalg.norm(i.centroid.values - e.values))
        e.cluster_id = (distance.tolist().index(min(distance)))
        for i in clusters.cluster:
            if(i.cluster_id == e.cluster_id):
                i.values = np.append(i.values, e)
            

def CalculateNewCentroid(clusters):
    #start with cluster number 
    for i in clusters.cluster:
        sum = 0
        average = 0
        for e in i.values:
            sum += e.values
        average = (sum / len(i.values))
        if (abs(average - i.centroid.values) < THRESHOLD).any():
            return False  
        elif (abs(average - i.centroid.values) >= THRESHOLD).any():
            i.centroid.values = average
            return True
        
def ClearCluster(clusters):
    for i in clusters.cluster:
        i.values = np.array([])

def KMeansHub(dataset, kvalue):
    tempvalue = True
    #Generates the first clusters and initial centroids 
    clusters = GenerateRandomCentroid(dataset, kvalue)
    #Cluster the values
    Cluster(dataset, clusters)

    while(tempvalue):
        tempvalue = CalculateNewCentroid(clusters)
        if(tempvalue):
            ClearCluster(clusters)
            Cluster(dataset, clusters)
    

    return clusters