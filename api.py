from flask import Flask, request, jsonify
import markdown.extensions.fenced_code
#import src.getdata as get
import json
import src.post as post
import src.get as get
import pprint


app =Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def index():
    readme_file =open('README.md','r')
    md_template_string = markdown.markdown(readme_file.read(), extensions =['fenced_code'])
    return md_template_string


@app.route('/line/<character>')
def random_line(character):
    return jsonify(get.random_message_character(person))


@app.route('/scene/<scene_id>')
def get_scene(scene_id):

    season =request.args.get('season', -1) #this is optional
    episode =request.args.get('episode', -1) #this is optional
    limit =request.args.get('limit', 1) #this is optional


    return jsonify(get.scene(scene_id, season, episode, limit))

@app.route('/list/<item>')
def get_list(item):

    season =request.args.get('season', -1) #this is optional
    episode =request.args.get('episode', -1) #this is optional


    return jsonify(get.list_items(item, season, episode))







##################### POST  ENDPOINTS  ##########################################################

@app.route('/newscene', methods=['POST'])
def post_scene():
    '''
    Post method to create a new scene (document) to database.
    Args:


    '''

    try:
        season = request.args['season']
        episode = request.args['episode']
        episode_name =request.args.get('episode_name') #this is optional

    except:
        return 'Error. Missing a required parameter. Please check API documentation.'

    inserted_id = post.insert_scene(season, episode, episode_name)

    return f'New scene was succesfully created, with ObjectID = {inserted_id}'

@app.route('/newperson', methods=['POST'])
def post_person():
    try:
        _id = request.args['id']
        person = request.args['person']

    except:
        return 'Error. Missing a required parameter. Please check API documentation.'

    check = post.insert_person(_id, person)

    return check


@app.route('/newline', methods=['POST'])
def post_line():
    try:
        _id = request.args['id']
        person = request.args['person']
        line = request.args['line']

    except:
        return 'Error. Missing a required parameter. Please check API documentation.'

    check = post.insert_line(_id, person, line)

    return check




    







app.run(debug=True)