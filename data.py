import pandas as pd
import numpy as np

#read csv file 
full_dataset = pd.read_csv("Longotor1delta.csv")
actual_dataset = pd.read_csv("interested_genes.csv")

#id of the datapoints
public_id = full_dataset.iloc[:, 0].to_numpy()
canidate_genes = actual_dataset.iloc[:, 0].to_numpy()

#gene name 
gene = full_dataset.iloc[:, 1].to_numpy()
known_genes = actual_dataset.iloc[:, 1].to_numpy()

#attributes of gene  
attributes = full_dataset.iloc[:, 3:6].to_numpy()



# Object to store all values of a datapoint 
class DataSet:
    def __init__(self):
        self.data = np.array([])

class DataPoint:
    def __init__(self):
        self.type = ""
        self.key = 0
        self.values = np.array([np.array([])])
        self.cluster_id = 0
        self.candidate = False
        self.known = False

class ClusterTree:
    def __init__(self):
        self.clusters = np.array([np.array([])])

class Clusters:
    def __init__(self):
        self.cluster = np.array([])
        self.amount = 0
        self.averagedistance = 0

class Cluster:
    def __init__(self):
        self.cluster_id = 0
        self.values = np.array([np.array([])])
        self.centroid = np.array([np.array([])])


# Populate data object
def StructData(DataSet):
    # set empty array 
    dataset = []

    # for the number of elements in the file, set the type, key, and values of each point and populate said point
    for i in range(len(public_id)): 
        if gene[i] in canidate_genes or public_id[i] in canidate_genes: 
            d = DataPoint()
            d.type = public_id[i]
            d.key = gene[i]
            d.values = attributes[i]
            d.candidate = True
            dataset.append(d)
        elif gene[i] in known_genes or public_id[i] in known_genes:
            d = DataPoint()
            d.type = public_id[i]
            d.key = gene[i]
            d.values = attributes[i]
            d.known = True
            dataset.append(d)

    #Sets the arrays within the DataSet object to the newly populated arrays 
    DataSet.data = np.array(dataset)

    return DataSet



def StructDataForHClustering(DataSet, Clusters):
    # set empty array 
    dataset = []

    # for the number of elements in the file, set the type, key, and values of each point and populate said point
    for i in DataSet.data: 
        d = Cluster()
        d.centroid = i
        dataset.append(d)

    #Sets the arrays within the DataSet object to the newly populated arrays 
    Clusters.cluster = np.array(dataset)

    return Clusters


def GetData():
    #Create new dataset object
    Dataset = DataSet()
    #Format the data
    FormattedData = StructData(Dataset)
    FindMinandMax(FormattedData)
    return FormattedData

def GetDataForHClusering():
    #create new clusters object
    Cluster = Clusters()
    dataset = GetData()
    Formatteddata =  StructDataForHClustering(dataset, Cluster)


    return Formatteddata



def FindMinandMax(FormattedData):
    temparray = np.zeros((len(FormattedData.data), 3))

    for k in range(3):

        for i, row in enumerate(FormattedData.data):
            temparray[i, k] = row.values[k]

        minimum = np.min(temparray[:, k])
        maximum = np.max(temparray[:, k])

        for i in range(len(FormattedData.data)):
            FormattedData.data[i].values[k] = (temparray[i, k] - minimum) / (maximum - minimum)

