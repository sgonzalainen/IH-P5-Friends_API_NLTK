from src.config import db, collection
from bson.objectid import ObjectId

def insert_scene(season, episode, episode_name = None):
    




    dict_insert = {'episode':{'season': f'{season}', 
    'number':f'{episode}',
    'name': f'{episode_name}'}}

    result = collection.insert_one(dict_insert)
    inserted_id = result.inserted_id

    return inserted_id



def insert_person(_id, person):


    response = collection.find_one({'_id': ObjectId(_id)},{'attendees': 1})
    attendees = response.get('attendees')

    if attendees is None:
        attendees =[person]
    elif person in attendees:
        return f'{person} is already as attendee in the scene with ObjectID = {_id}'

    else:
        attendees.append(person)

    collection.update_one({'_id': ObjectId(_id)}, {'$set': {'attendees': attendees}})

    return f'New person was succesfully inserted to scene with ObjectID = {_id}'


def insert_line(_id, person, line):

    new_entry = {'speaker': person, 'line': line}

    #if person is not as attendee, it cannot be inserted
    response = collection.find_one({'_id': ObjectId(_id)},{'attendees': 1})
    attendees = response.get('attendees')

    if isinstance(attendees, list) and person in attendees:
        pass
    else:
        return f'Line of {person} saying "{line}" could not be inserted because {person} is not listed as attendee.\nPlease ensure the character is as attendee first'

    #After checking, person is in attendees list now check if same line already exists
    response = collection.find_one({'_id': ObjectId(_id)},{'script': 1})
    script = response.get('script')

    if isinstance(script, list):
        for item in script:
            if person == item['speaker'] and line == item['line']: #if True means it is already in database
                return f'The line of {person} saying "{line}" already exists in the scene with ObjectID = {_id}'

        script.append(new_entry)

    else:
        script = [new_entry]

    collection.update_one({'_id': ObjectId(_id)}, {'$set': {'script': script}})

    return f'{person} saying "{line}" was succesfully inserted to scene with ObjectID = {_id}'


