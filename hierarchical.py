import data as d
import pandas as pd
import numpy as np


def hierarchical_clustering(dataset):

    # use clustered_data to modify values instead of actual dataset
    clustered_data = np.copy(dataset)
    iteration_count = 0  # for later use?

    """Not sure how to get the amount of clusters that we have per iteration... length of dataset will not work"""

    # While the amount of clusters > 1, we want to cluster them together and count iterations
    while (len(clustered_data.data > 1)):
        smallest = 9999  # Random large value prior to going through set
        for x in clustered_data.data:  # for every item in dataset
            for j in clustered_data.data:  # check it against every other item
                # if distance = 0 then they are same point? fix
                if np.linalg.norm(x-j) == 0:
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

        # add the new "centroid" / Average between two points
        clustered_data = np.append(clustered_data, np.mean(dataset.data[small1, small2]))
        # remove smallest point 1 - Since centroid is replacing them
        clustered_data = np.delete(clustered_data, dataset.data[small1])
        # remove smallest point 2 - Since centroid is replacing them
        clustered_data = np.delete(clustered_data, dataset.data[small2])
        # add one to iteration_count
        iteration_count += 1
