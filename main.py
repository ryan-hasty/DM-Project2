import data as data
import kmeans as kmeans
import analysis as any
import hybrid as h


def main():
    dataset = data.GetData()

    kvalue = input("How many clusters would you like to test?: ")
    kvalue = int(kvalue)
    results = kmeans.KMeansHub(dataset, kvalue)
    #any.PlotClusters(results, kvalue)


    heightValue = input("What height would you like to use?: ")
    heightValue = int(heightValue)
    temp = h.HierarchicalHub(results)

    temp = temp.clusters[heightValue]
    



    any.GeneStats(results)
    any.GeneStatsHybrid(temp)

main()