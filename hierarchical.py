import data as d
import pandas as pd
import numpy as np


def hierarchical_clustering(dataset):
    clustered_data = []
    smallest = 9999  # Random large value prior to going through set
    for x in dataset.data:  # for every item in dataset
        for j in dataset.data:  # check it against every other item
            if np.linalg.norm(x-j) == 0:  # if distance = 0 then they are same point? fix
                continue
            else:
                # if it's smaller then the current smallest distance
                if np.linalg.norm(x-j) < smallest:
                    # then it's the new smallest distance
                    smallest = np.linalg.norm(x-j)
                    # get indexes of smallest variables
                    small1 = np.where(dataset == x)
                    # get indexes of smallest variables
                    small2 = np.where(dataset == j)
        # Add the point to the clustered points if it makes it here.
        clustered_data.append(clustered_data, x)

    # add the new "centroid" / Average between two points
    np.append(clustered_data, np.mean(dataset.data[small1, small2]))
    # remove smallest point 1 - Since centroid is replacing them
    np.delete(clustered_data, dataset.data[small1])
    # remove smallest point 2 - Since centroid is replacing them
    np.delete(clustered_data, dataset.data[small2])
