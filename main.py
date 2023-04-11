import data as data
import kmeans as kmeans



def main():
    count1 = 0
    count2 = 0
    count3 = 0

    dataset = data.GetData()

    kvalue = input("How many clusters would you like to test?: ")
    kvalue = int(kvalue)
    centroid = kmeans.GenerateRandomCentroid(dataset, kvalue)
    results = kmeans.Cluster(dataset, centroid)

    for i in results.data: 
        if(i.cluster_id == 0):
            count1 += 1
        elif(i.cluster_id == 1): 
            count2 += 1
        elif(i.cluster_id == 2): 
            count3 += 1

    print("cluster1: ", count1)
    print("cluster2: ", count2)
    print("cluster3: ", count3)


        

main()