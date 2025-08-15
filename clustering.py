#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 22:11:27 2024

@author: lisaiizuka
"""
import numpy as np
import matplotlib.pyplot as plt

def distance(point1, point2):
    point1 = np.array(point1)
    point2 = np.array(point2)
    return np.sqrt(np.sum((point1 - point2)**2))
class Clustering:
    def __init__(self, words, embeddings):
        self.words = words
        self. embeddings = embeddings
        self.clusters = None
        self.centroids = None
        np.random.seed(7)
        
    def initialize_centroids(self, k): #k is the number of clusters;
        n = self.embeddings.shape[0] #total number of rows in embeddings
        numitems = np.random.choice(n, k, replace = False) #randomly select k unique values from 0 to n-1
        self.centroids = self.embeddings[numitems] #update the centroids with selected embeddings
        
    def assign_to_clusters(self):
        #initialize an array to store the cluster assignments for each pt
        self.clusters = np.zeros(len(self.words),dtype=int) 
        #loop through each data pt
        for i in range(self.embeddings.shape[0]):
            point1 = self.embeddings[i]
            min_dist = float('inf') #initialize the smallest value w a large value for later comparison
            nearest_centroid = -1 #initialize the index of the nearest centroid
            #loop through each centroid to find the closest one
            for j in range(self.centroids.shape[0]):
                point2 = self.centroids[j]
                dist = distance(point1, point2)
                if dist<min_dist: #update if we find a smaller distance
                    min_dist = dist
                    nearest_centroid = j
            self.clusters[i] = nearest_centroid #assign data pt to nearest centroid
            
    def compute_new_centroids(self):
         k = self.centroids.shape[0] #number of clusters
         d = self.embeddings.shape[1] #dimensinality of each embedding
         new_centroids = np.zeros((k,d)) #initialize a new 2d array  w k rows and d columns to store the updated centroids
         for i in range(k): #for each cluster
             #find indices of data pts that belong to cluster (i)
              points_in_cluster = self.embeddings[self.clusters == i]
              if len(points_in_cluster) > 0: #check for divsion by zero
                  #calculate the mean along each dimension
                  new_centroids[i] = np.mean(points_in_cluster, axis = 0)
              else: #for empty clusters, keep the centroid the same
                  new_centroids[i] = self.centroids[i]
         #update centroids with the new values
         self.centroids = new_centroids
         
    def kmeans(self, num_clusters, max_iterations):
        self.initialize_centroids(num_clusters)
        converged = False #set a flag for convergence
        i = 0 #initialize a counter so that it doesn't surpass the max_iterations
        while not converged and i < max_iterations:
            old_centroids = self.centroids.copy()
            #assign pts to nearest centroids and update centroids
            self.assign_to_clusters()
            self.compute_new_centroids()
            #check for convergence
            if np.allclose(self.centroids, old_centroids):
                converged = True #set the flag if centroids don't change
            #exit loop if converged, otherwise contunue
            i += 1
                
            
    def plot_words(self):
        plt.figure(figsize=(10,10))
        plt.scatter(self.embeddings[:,0], self.embeddings[:,1], marker='x')#plt the embeddings as pts
        #add text labels for each word
        for i in range(len(self.words)):
            word = self.words[i]
            plt.text(self.embeddings[i,0], self.embeddings[i,1], word, fontsize = 12) #place word at its corresponding coordinates
        plt.xlabel("Dimension 0")
        plt.ylabel("Dimension 1")
        plt.title("Word Embeddings")
        plt.savefig("words.png") #save plot to a file
        plt.show()

    def plot_clusters(self):
        plt.figure(figsize=(10,10))
        #define colors for clusters (one color per cluster)
        colors = ['b','g','y','r','k']
        #plot each word with the color of its assigned cluster
        for i in range(len(self.words)):
            #determine the color for the current word based on its assigned cluster
            plt.scatter(self.embeddings[i, 0], self.embeddings[i, 1], color=colors[self.clusters[i] % len(colors)], marker='x') #plt the word as 'x'
            plt.text(self.embeddings[i, 0], self.embeddings[i, 1], self.words[i], fontsize=12)#add the word label at its position
        #plot each centroid with the same color as its cluster
        for j in range(self.centroids.shape[0]):
            # Determine the color for the centroid to match the points in its cluster
            cluster_color = colors[j % len(colors)]
            # Plot the centroid as a solid dot ('o') at its (x, y) coordinates
            plt.scatter(self.centroids[j, 0], self.centroids[j, 1], color=cluster_color, marker='o', s=100)  # centroid
        plt.xlabel("Dimension 0")
        plt.ylabel("Dimension 1")
        plt.title("Word Embeddings and K-means Clusters")
        plt.savefig("clusters.png") # Save the plot to a file named "clusters.png"
        plt.show()
            
            
        
            
                     
                 
             
            
                
                
        
    
        
    