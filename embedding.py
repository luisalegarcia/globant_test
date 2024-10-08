""" Vectorizer text with different techniques """
# import libraries
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import gensim.downloader as api

def doc2vec(words:str, model) -> np.array:
    """" function that recieves a list of words 
        and a word embedding and return a vector
        with 300 dimensions."""
    # Tokenize
    words = word_tokenize(words)
    # begin vector in 0s
    feature_vector = np.zeros((300,), dtype="float64")
    # count valid words
    n_words = 0
    # sum all vectors from each word and divede by the total.
    for word in words:
        try:
            feature_vector = np.add(feature_vector, model[word])
            n_words += 1
        except: 
            pass
        if n_words:
            feature_vector = np.divide(feature_vector, n_words)
    return feature_vector.reshape(1,300)


def embedding(data:pd.DataFrame, column:str, embedding : str) -> np.array:
    if embedding == "TF-IDF":
        # TF IDF vectorizer
        vectorizer = TfidfVectorizer(max_df=0.95) 
        text_vec = vectorizer.fit_transform(data[column])
        text_vec = text_vec.toarray()
        return text_vec
    elif embedding == "word2vec":
        # upload pre trained embedding
        word2vec_model = api.load("word2vec-google-news-300")
        # loop to create the vector for each document.
        text_vec = []
        for i in range(len(data)):
            temp = doc2vec(data[column].iloc[i], word2vec_model)
            text_vec.append(temp)
        text_vec = np.array(text_vec)
        text_vec = text_vec.reshape(len(data),300)
        return text_vec
    elif embedding == 'glove':
        # upload pre trained embedding
        glove_model = api.load('glove-wiki-gigaword-300')
        # loop to create the vector for each document.
        text_vec = []
        for i in range(len(data)):
            temp = doc2vec(data[column].iloc[i], glove_model)
            text_vec.append(temp)
        text_vec = np.array(text_vec)
        text_vec = text_vec.reshape(len(data),300)
        return text_vec

