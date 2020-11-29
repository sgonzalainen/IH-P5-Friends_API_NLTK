import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import numpy as np
from textblob import TextBlob



def remove_symbols(text):

    words = nltk.word_tokenize(text)
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    return tokens

def remove_stop_words(tokens):

    stop_words = set(stopwords.words('english'))
    tokens_clean = [e for e in tokens if e not in stop_words]

    return tokens_clean



def analyze_sentiment(text):

    sia = SentimentIntensityAnalyzer()
    polarity = sia.polarity_scores(text)
    pol = polarity['compound']

    return pol


## Not in useeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
def calculate_sentiment(mylist):

    tmp_list = [analyze_sentiment(item) for item in mylist]

    return round(np.array(tmp_list).mean(),2)

def analyze_sentiment_blob(text):

    en_blob=TextBlob(u'{}'.format(text))

    
    return en_blob.sentiment.polarity








