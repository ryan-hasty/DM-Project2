import pandas as pd
import numpy as np

#read csv file 
full_dataset = pd.read_csv("Longotor1delta.csv")

#id of the datapoints
public_id = full_dataset.iloc[:, 0].to_numpy()

#gene name 
gene = full_dataset.iloc[:, 1].to_numpy()

#attributes of gene  
attributes = full_dataset.iloc[:, 3:6].to_numpy()

# Object to store all values of a datapoint 
class DataPoint:
    def __init__(self):
        self.type = ""
        self.key = 0
        self.values = np.array([])
        self.prediction_keys = np.array([])

class DataSet:
    def __init__(self):
        self.data = np.array([])


# Populate data object
def StructData(DataSet):
    # set empty array 
    dataset = []

    # for the number of elements in the file, set the type, key, and values of each point and populate said point
    for i in range(len(public_id)): 
        d = DataPoint()
        d.type = public_id[i]
        d.key = gene[i]
        d.values = attributes[i]
        dataset.append(d)

    #Sets the arrays within the DataSet object to the newly populated arrays 
    DataSet.data = np.array(dataset)

    return DataSet


def GetData():
    #Create new dataset object 
    Dataset = DataSet()
    #Format the data 
    FormattedData = StructData(Dataset)
    return FormattedData
