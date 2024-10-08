""" Cleaning text from special characters and others"""
# import libraries
import pandas as pd
import nltk
from nltk.corpus import stopwords
import re
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")  

# custom clean function
def clean_text(text:str) -> str:
    #ps = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    # all words to lowercase
    text = text.lower()
    # clean special characters
    text = re.sub(r'[^\w\s]', '', text)
    # tokenize
    words = word_tokenize(text)
    # remove stop words
    words = [word for word in words if word.lower() not in stop_words]
    # lemmatize words
    Words = [lemmatizer.lemmatize(word) for word in words]
    text = ' '.join(Words)   
    return text

def preprocess(data:pd.DataFrame, column:str) -> pd.DataFrame:
    # apply function
    data[column] = data[column].apply(clean_text)
    return data
