""" Clustering with the word embeddings"""
# import libraries
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering

def clustering (X:np.ndarray,  cluster) -> np.ndarray:
    if cluster == 'kmeans':
        # make cluster, 6 because discover in notebook 
        kmeans = KMeans(n_clusters=6, init='k-means++')
        return kmeans.fit_transform(X)
    elif cluster == "ward":
        # make cluster, 5 because discover in notebook
        clustering = AgglomerativeClustering(n_clusters = 5,linkage="ward")
        return clustering.fit_predict(X)



