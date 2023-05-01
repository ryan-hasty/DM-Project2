import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sys

def PlotClusters(clusters, num_clusters):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Define a color dictionary to assign a color to each label
    color_dict = {}
    color_list = plt.cm.Set1(np.linspace(0, 1, num_clusters))
    for i in range(num_clusters):
        label = 'Cluster ' + str(i)
        color_dict[label] = color_list[i]

        # Plot the points in the cluster with the corresponding color
        for j, e in enumerate(clusters.cluster[i].values):
            ax.scatter(e.values[0], e.values[1], e.values[2], color=color_dict[label])

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    # Create a custom legend with the colors assigned to each label
    handles = []
    for label, color in color_dict.items():
        handles.append(plt.Line2D([], [], color=color, marker='o', linestyle='None', label=label))
    ax.legend(handles=handles)

    plt.show()

def GeneStats(clusters):
    count = 1
    with open("kmeans.txt", "w") as f:
        f.truncate(0)  # Clears the file contents
        for i in clusters.cluster:
            known = 0
            candidate = 0
            sys.stdout = f
            print("Cluster " + str(count))
            print("{")
            count += 1
            for idx, e in enumerate(i.values):
                if e.known == True:
                    known+= 1
                    if (idx + 1) % 25 == 0:
                        print(e.type + "(KNOWN)")
                        print()
                    else:
                        print(e.type + "(KNOWN)", end=", ")
                elif e.candidate == True:
                    candidate += 1
                    if (idx + 1) % 25 == 0:
                        print(e.type + "(CANIDATE)")
                        print()   
                    else:
                        print(e.type + "(CANIDATE)", end=", ")
            print("Number of Canidate Genes", candidate, "Number of known genes", known, "Ratio", known/candidate, "}")



def GeneStatsHybrid(clusters):
    count = 1
    with open("hybrid.txt", "w") as f:
        f.truncate(0)  # Clears the file contents
        for i in clusters.cluster:
            sys.stdout = f
            print("Cluster " + str(count))
            print("{")
            count += 1
            for idx, e in enumerate(i.values):
                if (idx + 1) % 100 == 0:
                    print(e.type)
                    print()
                else:
                    print(e.type, end=", ")
            print("}")


