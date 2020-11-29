from src.config import db, collection
from bson.objectid import ObjectId

def insert_scene(season, episode, episode_name = None):
    '''
    Creates a new document to MongoDb collection
    Args:
        season(str): number of season.
        episode(str): episode number
        episode_name (str): name of episode
    Returns:
        inserted_id(str): ObjectID number MongoDb document

    '''

    dict_insert = {'episode':{'season': f'{season}', 
    'number':f'{episode}',
    'name': f'{episode_name}'}}

    result = collection.insert_one(dict_insert)
    inserted_id = result.inserted_id

    return inserted_id



def insert_person(_id, person):
    '''
    Includes a character as atendee in attendees field of a MongoDB document
    Args:
        _id(str): ObjectID number MongoDb document
        person(str): character name
    Return:
        Sucess or error message

    '''

    try:
        response = collection.find_one({'_id': ObjectId(_id)},{'attendees': 1})
        check = response['attendees']
    except:
        return f'{_id} is an invalid id'
    else:

        attendees = response.get('attendees')

        if attendees is None:
            attendees =[person]
        elif person in attendees:
            return f'{person} is already as attendee in the scene with ObjectID = {_id}'

        else:
            attendees.append(person)

        collection.update_one({'_id': ObjectId(_id)}, {'$set': {'attendees': attendees}})

        return f'{person} was succesfully inserted to scene with ObjectID = {_id}'


def insert_line(_id, person, line):
    '''
    Includes a script line in script field of a MongoDB document
    Args:
        _id(str): ObjectID number MongoDb document
        person(str): character name
        line(str): script line
    Return:
        Sucess or error message


    '''

    new_entry = {'speaker': person, 'line': line}

    #if person is not as attendee, it cannot be inserted

    try:
        response = collection.find_one({'_id': ObjectId(_id)},{'attendees': 1})
        check = response['attendees']
    except:
        return f'{_id} is an invalid id'
    else:

        attendees = response.get('attendees')

        if isinstance(attendees, list) and person in attendees:
            pass
        else:
            return f'Line of {person} saying "{line}" could not be inserted because {person} is not listed as attendee. Please ensure the character is as attendee first'

        #After checking, person is in attendees list now check if same line already exists
        response = collection.find_one({'_id': ObjectId(_id)},{'script': 1})
        script = response.get('script')

        if isinstance(script, list):
            script.append(new_entry)

        else:
            script = [new_entry]

        collection.update_one({'_id': ObjectId(_id)}, {'$set': {'script': script}})

        return f'{person} saying "{line}" was succesfully inserted to scene with ObjectID = {_id}'


