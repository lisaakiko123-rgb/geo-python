#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:37:34 2024

@author: lisaiizuka
"""

import pandas as pd
import numpy as np
from clustering import Clustering

#load the data
data = pd.read_csv("embeddings.csv")
words = data["word"].tolist()
embeddings = data[["dim0", "dim1"]].to_numpy()

#instantiate a clustering object
clustering = Clustering(words, embeddings)

#plot initial word embeddings
clustering.plot_words

#set clustering parameters and run the K-means algorithm
num_clusters = 3 
max_iterations = 8
clustering.kmeans(num_clusters, max_iterations)

#plot the clustered results
clustering.plot_clusters()

"""
response: 
the blue cluster is clustered together by a neg/neutral quality.
the yellow cluster is clustered together by positive qualities
the green cluster is clustered together by highly pos qualities (very praising)

"""
           