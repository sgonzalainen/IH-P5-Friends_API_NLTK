import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import numpy as np
from textblob import TextBlob



def remove_symbols(text):
    '''
    Function to remove symbols from text
    Args:
        text(str): text
    
    Returns:
        tokens(list): list of words without symbols

    '''

    words = nltk.word_tokenize(text)
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    return tokens

def remove_stop_words(tokens):
    '''
    Remove stop words in English
    Args:
        tokens(list): list of words

    Returns:
        tokens_clean(list): list of words without stop words

    '''

    stop_words = set(stopwords.words('english'))
    tokens_clean = [e for e in tokens if e not in stop_words]

    return tokens_clean


def analyze_sentiment_blob(text):
    '''
    Gets polarity score given a text
    Args:
        text(str): text

    Returns:
        polarity score from blobtext 

    '''

    en_blob=TextBlob(u'{}'.format(text))

    
    return en_blob.sentiment.polarity








