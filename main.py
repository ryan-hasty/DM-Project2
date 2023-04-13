import data as data
import kmeans as kmeans
import analysis as any


def main():
    dataset = data.GetData()

    kvalue = input("How many clusters would you like to test?: ")
    kvalue = int(kvalue)
    results = kmeans.KMeansHub(dataset, kvalue)
    any.GeneStats(results)
    #any.PlotClusters(results, kvalue)

main()