import data as data
import kmeans as kmeans
import analysis as any
import hierchical as h


def main():
    dataset = data.GetData()
    hdataset = data.GetDataForHClusering()

    kvalue = input("How many clusters would you like to test?: ")
    kvalue = int(kvalue)
    results = kmeans.KMeansHub(dataset, kvalue)
    #any.PlotClusters(results, kvalue)

    temp = h.HierarchicalHub(hdataset)

    last_element = temp.clusters[-1]

    
    any.GeneStats(results)
    any.GeneStatsHybrid(last_element)

main()