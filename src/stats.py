import pandas as pd 
import requests
from collections import Counter 


def get_sentiment_all_char():
    '''
    Gets overall sentiment score for all characters in collection
    Args:

    Returns:
        score_list(list): list containing a dictionary with info

    '''
    endpoint = 'http://localhost:5000/list/character'
    r = requests.get(endpoint)
    characters = r.json()
    score_list = []
    for character in characters:
        endpoint = f'http://localhost:5000/sentiment/character/{character}'
        r = requests.get(endpoint)
        score_list.append(r.json()[0])

    return score_list


def get_appearances_char():
    '''
    Counters number of appearances (i.e. episodes) of all characters
    Args:

    Returns:
        Dictionary with info
    '''
    tmp_list = []

    endpoint = 'http://localhost:5000/list/season'
    seasons = requests.get(endpoint).json()
    for season in seasons:
        endpoint = 'http://localhost:5000/list/episode'
        params = {'season': season}
        episodes = requests.get(endpoint, params=params).json()

        for episode in episodes:
            endpoint = f'http://localhost:5000/list/character'
            params = {'season':season, 'episode': episode}
            r = requests.get(endpoint, params = params)
            tmp_list.extend(r.json())

    return Counter(tmp_list)

def get_sentiment_recurrent_char(number):
    '''
    Get sentiment scores for only characters appearing at least number of episodes specified.
    Args:
        number(int): number of episodes

    Returns:
        score_list(list): list containing a dictionary with info
    '''

    mydict = get_appearances_char()

    characters = [key for key,value in mydict.items() if value >= number]

    score_list = []
    for character in characters:
        endpoint = f'http://localhost:5000/sentiment/character/{character}'
        r = requests.get(endpoint)
        score_list.append(r.json()[0])
    
    return score_list

def get_sentiment_main_chars_per_episode(**main_characters):
    '''
    Get sentiment scores of main characters of friends per episode
    Args:
        main_characters: list of characters to study

    Returns:
        tmp_list(list): list containing a dictionary with info

    '''


    
    endpoint = 'http://localhost:5000/list/season'
    seasons = requests.get(endpoint).json()
    seasons = sorted(seasons, key = lambda x: int(x))


    tmp_list = []

    for season in seasons:
        endpoint = 'http://localhost:5000/list/episode'
        params = {'season': season}
        episodes = requests.get(endpoint, params=params).json()
        episodes = sorted(episodes, key = lambda x: int(x))
        for episode in episodes:
            for character in main_characters:

                endpoint = f'http://localhost:5000/sentiment/character/{character}'
                params = {'season':season, 'episode': episode}
                score = requests.get(endpoint, params = params).json()[0]['sentiment_score']


                tmp_dict = {'character': character, 'season': season, 'episode': episode, 'sentiment_score': score}
                tmp_list.append(tmp_dict)

    return tmp_list







    




