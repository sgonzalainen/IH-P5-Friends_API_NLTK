import os
import re
import requests
import src.sentiment as sent
from src.config import db, collection


def create_scene(season, episode, episode_name = None):

    '''
    Function to create a scene, MongoDB document from Kaggle dataset
    Args:
        season(str): season number
        episode(str): episode number
        episode_name (str): name of episode

    Returns:
        inserted_id(str): ObjectID number MongoDb document

    '''
    
    
    params= {'season':season, 'episode':episode, 'episode_name': episode_name}
    endpoint = 'http://localhost:5000/newscene'
    
    r = requests.post(endpoint, params = params)
    
    response = r.text
    print(response)
    
    inserted_id = response.split('= ')[1]
    
    return inserted_id

def insert_person(_id, person):
    '''
    Includes a character as atendee in attendees field of a MongoDB document from Kaggle dataset
    Args:
        _id(str): ObjectID number MongoDb document
        person(str): character name

    Returns:
        
    '''
    
    params= {'id':_id, 'person':person}
    endpoint = 'http://localhost:5000/addperson'
    
    r = requests.post(endpoint, params = params)
    response = r.text
    print(response)


def insert_line(_id, person, line):
    '''
    Includes a script line in script field of a MongoDB document from Kaggle dataset
    Args:
        _id(str): ObjectID number MongoDb document
        person(str): character name
        line(str): script line

    Returns: 

    '''

    
    params= {'id':_id, 'person': person,'line': line}
    endpoint = 'http://localhost:5000/addline'
    
    r = requests.post(endpoint, params = params)
    response = r.text
    print(response)


def new_line_hanlder(_id, match, attendees):
    '''
    Given a match a new script line in txt file, finds person and line to insert to collection.
    Args:
        _id(str): ObjectID number MongoDb document
        match(regex match)
        attendees(list): list of attendees(field) in a Mongodb document

    Returns:
        attendees(list): updated list of attendees(field) in a Mongodb document after new line insertion.

    '''
    
    person = match[1].capitalize()
    person = fix_person(person)

    line = re.sub('\(.+?\)','',match[2]).replace('"','').strip()
    
    if person not in attendees:
        insert_person(_id, person)
        attendees.append(person)
        
    insert_line(_id, person, line)
    
    
    return attendees


def scrape_dataset(path):
    '''
    Main function to call to scrape Kaggle dataset txt files and insert to Mongodb collection
    Args:
        path(str): path to txt files

    Returns:

    '''

    
    files = sorted(os.listdir(path))
    for file in files:
    
        season = int(file[1:3])
        episode = int(file[4:6])
        episode_name = file.split(' ',1)[1].split('.txt',1)[0]

        print(f'NEW EPISODE SEASON {season}, EPISODE {episode}')
        
        f = open(f'{path}{file}', "r")
        
        attendees = []
        
        for line in f:
            
            if line.startswith('[Scene:'):
                inserted_id = create_scene(season,episode,episode_name)
                attendees = []
                continue
            
            elif re.match(r'^(\w+):',line) != None:
                match = re.match(r'^(\w+):(.+)', line)
                attendees = new_line_hanlder(inserted_id, match, attendees)


def fix_person(person):
    '''
    Mini function to fix typing mistakes in main characters
    Args:
        person(str): character name

    Returns:
        person(str): fixed character name


    '''

    if person == 'Chandlers' or person == 'Chan':
        return 'Chandler'
    elif person == 'Racel' or person =='Rach' or person == 'Rache' or person == 'Rahcel':
        return 'Rachel'
    elif person == 'Mnca':
        return 'Monica'
    elif person == 'Phoe':
        return 'Phoebe'
    else:
        return person



    
def include_sentiment_score():
    '''
    Function to call to include sentiment score in all documents of a MongoDB collection.
    Args:

    Returns:

    '''
    
    scenes = list(collection.find({}))

    for scene in scenes:

        _id = scene.get('_id')

        tmp_list = []
        if isinstance(scene.get('script'),list):
            for line in scene.get('script'):
                string = line.get('line')

                tokens = sent.remove_symbols(string) #remove symbols
                clean_string = ' '.join(sent.remove_stop_words(tokens))

                score = round(sent.analyze_sentiment_blob(clean_string),3)
                print(string, score)
                tmp_list.append({'speaker': line.get('speaker'), 'line': line.get('line'), 'sentiment_score': score})

        

            collection.update_one({'_id': _id}, {'$set': {'script': tmp_list}}) #updates document once all lines have been scored






    



