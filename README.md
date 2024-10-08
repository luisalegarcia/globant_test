# Document clusterization

The objective of this repo is to clusterize the documents from the next [link]( https://www.nsf.gov/awardsearch/download?DownloadFileName=2020&All=true). There will be different ways to achieve the objective through different embeddings and clustering techniques.

## Read files - Feature Selection 
To read the files, the python lxml package was used to extract information from each document. The variables that were extracted are title, abstract, directorate and division. This because they seem to be the variables with the most information to run the clustering.
Taking into account these variables, there will be duplicate data, however, considering that each text needs to be in a cluster, it was decided not to eliminate them.

## Preprocessing
This module cleans the text of a specific column, this cleaning includes, making a lemmatization, removing stop words and removin special characters. 

## Embedding

This is the war that we passes from words to numeric vectors, here it take into the count three embeddings techniques: 

1. Tf - idf vectorizer : This embedding technique takes into account the number of times a term appears in a document contrasted with how many documents it appears in.  In this way the less common words are the ones that receive more weight.
2. word2vec: This is a model that looks for semantic similarities of words. In this case, a pre-trained model was used.
3. GloVe  (Global Vectors for Word Representation) :This embedding is trained taking into account all the contexts in which a word appears, not just one at a time. Also for this case a pre-trained model was used.

Apart from the tf idf, embedding techniques pass a single word to a vector, so to pass the whole document what is done is an average of the vectors of all the words in the document. 

## Clustering

Once each document has its vector representation, the clustering can be done. For this purpose, two clustering models were used

1. kmeans: is the most common clustering technique which seeks to minimize the distance of the vectors between the cluster elements.
2. Aglomerative clustering: This, unlike kmeans, starts with the number of clusters equal to the number of observations and then groups them by means of a distance, in this case the Ward distance was used. 

The rationale for the selection of the cluster number can be found in the no_cluster_selection.ipynb

## Topics

In order to find the topics discussed in the papers we used Latent Dirichlet Allocation (LDA). Which is a multivariate technique that seeks to relate one or more topics to each document according to the frequency with which each word appears. Unfortunately, due to lack of time, it was not possible to perform a depth analysis. 

## Conclusion 

Although the quality metrics on the clusters were partially observed. It was a standardized and modularized pipeline with the opportunity to add more embeddings and clustering techniques in a simple way without affecting the code architecture. 

Also due to a lack of time it was not possible to run all the combinations to find the clustering with the best metrics and to make the most sense.

## Future Work
So far only the abstract variable has been explored, but the other 3 variables that were selected at the beginning can provide important information for clustering. 
Finally add more and better embedding and clustering techniques since the ones used here are the most common and with mostly default parameters. 
