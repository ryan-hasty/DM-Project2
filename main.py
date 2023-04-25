import data as data
import kmeans as kmeans
import analysis as any
import hierarchical as h


def main():
    dataset = data.GetData()
    h.hierarchical_clustering(dataset)
    kvalue = input("How many clusters would you like to test?: ")
    kvalue = int(kvalue)
    results = kmeans.KMeansHub(dataset, kvalue)
    any.GeneStats(results)
    any.PlotClusters(results, kvalue)

main()