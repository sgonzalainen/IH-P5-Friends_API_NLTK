 <div style=><img src="https://camo.githubusercontent.com/52d2ff8778b60261533a7dba8dd989c6893a519b/68747470733a2f2f692e696d6775722e636f6d2f315167724e4e772e706e67"/></div>

# API Sentiment Project. 
# Creating my own API

 <div style="text-align:center"><img src="img/banner2.jpg" height=300 /></div>

The scope of [this Ironhack project](https://github.com/sgonzalainen/datamad1020-rev/tree/master/projects/W6-api-sentiment-project) is to create our own API in **Flask**, which should include text sentiment analysis data. Data is stored in **MongoDB** via requests POST methods.

## Introduction
My API is about script dialogues from TV Series **FRIENDS**. Data was taken from [this Kaggle dataset](https://www.kaggle.com/blessondensil294/friends-tv-series-screenplay-script).

## Description

* Data is stored in a MongoDB collection.
* Each MongoDB document is a scene. Find below example of a document.

```json
[
  {
    "_id": "5fc28496abbba8b12effa206", 
    "episode": {
      "season": "4", 
      "number": "14", 
      "name": "Joeys Dirty Day"
    }, 
    "attendees": [
      "Joey"
    ], 
    "script": [
      {
        "speaker": "Joey", 
        "line": "Hey! Joey Tribbiani! I’m here! I’m here!", 
        "sentiment_score": 0.0
      }, 
      {
        "speaker": "Joey", 
        "line": "Look at that, Charlton Heston eating a liquorice whip!", 
        "sentiment_score": 0.0
      }, 
      {
        "speaker": "Joey", 
        "line": "Whoa! Yeah, what the hell is that? What smells so bad?", 
        "sentiment_score": -0.7
      }, 
      {
        "speaker": "Joey", 
        "line": "Y’know, I can see why you think that, but ah, actually, you know who I think it is?", 
        "sentiment_score": 0.0
      }, 
      {
        "speaker": "Joey", 
        "line": "No-no, it’s uh, it’s Heston.", 
        "sentiment_score": 0.0
      }, 
      {
        "speaker": "Joey", 
        "line": "Yeah, the man wreaks! Smells like he went on a three day fishing trip and then ate some liquorice.", 
        "sentiment_score": 0.0
      }, 
      {
        "speaker": "Joey", 
        "line": "Really, a shower huh? And uh, which-which room might that be?", 
        "sentiment_score": 0.2
      }, 
      {
        "speaker": "Joey", 
        "line": "Interesting.", 
        "sentiment_score": 0.5
      }
    ]
  }
]
```

* All data inserted to MongoDB is done via POST methods.
* For instructions about endpoints for this API, please refer to API documentation in `index.md` .
* For sentiment analysis, the approach was to remove symbols and stop words with NLTK and get the sentiment analysis polarity with TextBlob.
* The Kaggle dataset (not included in this repo) contains a series of txt files. Each file is an episode. Below an extract of a txt file:

```
The One With The Fake Monica
Written by: Adam Chase and Ira Ungerleider


[Scene: Monica and Rachel's, everyone is looking at papers.]

Joey: How could someone get a hold of your credit card number?

Monica: I have no idea. But look how much they spent!

Rachel: Monica, would you calm down? The credit card people said that you only have to pay for the stuff that you bought.

Monica: I know. It's just such reckless spending.

Ross: I think when someone steals your credit card, they've kind of already thrown caution to the wind.

Chandler: Wow, what a geek. They spent $69.95 on a Wonder Mop.

```

## Repo Structure
* `api.py` : main file to run Flask app.
* `index.md`: API documentation.
* `notebooks`:

    * `requests.ipynb`: notebook where it is shown how all endpoints works via requests methods (along with some error tests).
    * `stats.ipynb`: practice use of the API. Notebook containing several data insights from API calls.
* `src`:

    * `config.py`: configuration file with the connection to MongoDB database.
    * `post.py`: auxiliary functions for POST methods.
    * `get.py`: auxiliary functions for GET methods.
    * `dataset.py`: functions to scrape the Kaggle dataset. Use of this functions not included in the notebooks on this repo.
    * `sentiment.py` : auxiliary functions for sentiment score analysis.
    * `stats.py`: auxiliary functions for insights in stats.ipynb . 
* `img`: folder containing gifs and pictures inserted in markdown files and notebooks. 

## Further developments
* Develop more endpoints
* Clean character names like 'all', 'guy', etc


## Technologies and Environment

Python3 on Ubuntu 20.04


### API
* __[Flask](https://pypi.org/project/Flask/)__
* __[pyMongo](https://pypi.org/project/pymongo/)__

### Sentiment Analysis
* __[NLTK](https://pypi.org/project/nltk/)__
* __[Textblob](https://pypi.org/project/textblob/)__

