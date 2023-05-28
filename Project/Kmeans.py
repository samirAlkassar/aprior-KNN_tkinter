from sklearn.datasets import make_blobs
import pandas as pd
import random as rd 
import numpy as np 
import matplotlib.pyplot as plt 

class Kmeans: 
    def __init__(self,n_clusters ):
        self.n_clusters = n_clusters
        self.centers = []
        self.clusters = {}
        self.distortion = []
    
    def initialize_centers(self, n_clusters:int, data:list ):
        centers = []
        indices = []
        while len(centers)< n_clusters:
            rand_point = rd.randint(0, len(data)-1) 
            if rand_point not in indices:
                indices.append(rand_point)
                center = data[rand_point]
                centers.append(center) 
                 
        return centers 
    
    def calc_distance(self, center, point):
        dis = np.subtract(center, point) 
        dis = dis**2 
        dis = np.sum(dis) 
        return dis 
    
    def make_clusters(self, centers, data): 
        clusters = {}
        clusters_distances_sum = 0
        for j in range(self.n_clusters):
            clusters[j] = []

        for idx, point in enumerate(data): 
            distances = [] 
            for  center in centers: 
                dis = self.calc_distance(center , point)
                distances.append(dis) 
            c = np.argmin(distances) 
            clusters[c].append(idx)
            clusters_distances_sum+= distances[c] 
        return clusters , clusters_distances_sum
    
    def update_centers(self, clusters, data): 
        new_centers = []
        for _, samples in clusters.items(): 
            new_center = np.sum([x for i, x in enumerate(data) if i in samples], axis=0) / len(samples)          
            new_centers.append(new_center) 
        return new_centers

    def fit(self , n_clusters,data) : 
        centers = self.initialize_centers(n_clusters, data) 
        clusters, distances = self.make_clusters(centers , data ) 
        self.distortion.append(distances)
        while True :
           
            new_centers  = self.update_centers(clusters ,data )      
            new_clusters,distances = self.make_clusters(new_centers , data)      
            if distances >= self.distortion[-1]:
                print(distances )
                break 
            centers = new_centers 
            clusters = new_clusters
            self.distortion.append(distances)
        self.centers = centers

    def predict(self,point): 
        distances = []
        for center in self.centers : 
            dis = self.calc_distance(center , point) 
            distances.append(dis) 
        return np.argmin(distances) 


dataset, _ = make_blobs(n_samples=200 , n_features=3 , centers=3 , cluster_std=0.5 , random_state=42)

# pd.DataFrame(dataset).to_csv('./dataset.csv')
# plt.xlabel('Iterations',fontsize = 12, color= 'b', fontweight = 'bold' ) 
# plt.ylabel('Distortion Values',fontsize = 12, color= 'b', fontweight = 'bold' ) 
# plt.title('The Distortion Function of Clusters',fontsize = 16, color= 'r', fontweight = 'bold')
# colors = ['r','g','b','y']
# for i in range(4):
#     model = Kmeans(3)
#     model.fit(3, dataset)  
#     plt.plot(np.array(model.distortion)/1000, marker = 'x', color = colors[i], linewidth = 3.0, markersize = 10, markeredgewidth =4) 
# plt.savefig('./results.png')
# plt.show()


