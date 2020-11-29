 

 <div style="text-align:center"><img src="https://blogstudio.s3.amazonaws.com/retrostyler/0de9af6d3791b02e2dd210e9603105f7.jpg" height=200 /></div>

# FRIENDS DIALOGUES API

Welcome to my Friends Dialogues API, where you could retrieve data related to script lines for all episodes of Friends. If wanted, you could also create a new scene and insert new dialogues.


# POST Requests

## New Scene

It creates a new scene by adding a new document into MongoDB database.

- Endpoint : http://localhost:5000/newscene
- Query Parameters: 
    - season (required)
    - episode (required)
    - episode_name (optional)

- Response: 
    - On success (example):
        - "New scene was succesfully created, with ObjectID = 5fc2845babbba8b12eff9eb3"
    - On error (example):
        - "Error. Missing a required parameter. Please check API documentation."

## Add Character

It includes a character into Attendee field  of a scene (i.e. a MongoDB document). If character already exists, it will raise a warning message.

- Endpoint : http://localhost:5000/addcharacter
- Query Parameters: 
    - id (required) : scene ObjectId
    - character (required) : name of character


- Response: 
    - On success (example):
        - "Rachel was succesfully inserted to scene with ObjectID = 5fc2845babbba8b12eff9eb3"
    - On error (example):
        - "Error. Missing a required parameter. Please check API documentation."
    * Warning: 
        - "Rachel is already as attendee in the scene with ObjectID = 5fc2845babbba8b12eff9eb3"
    
## Add Script Line

It includes a script line into script field of a scene (i.e. a MongoDB document). Warning, character must be inserted into Attendees field in advance.

- Endpoint : http://localhost:5000/addcharacter
- Query Parameters: 
    - id (required) : scene ObjectId
    - character (required) : name of character
    - line (required): text of the dialogue


- Response: 
    - On success (example):
        - "Rachel saying "Oh, that is so sick." was succesfully inserted to scene with ObjectID = 5fc2845babbba8b12eff9eb2"
    - On error (example):
        - "Error. Missing a required parameter. Please check API documentation."
        - "Line of Rachel saying "Oh, that is so sick." could not be inserted because Rachel is not listed as attendee. Please ensure the character is as attendee first".



# GET Requests

## Lists

Retrieves a list of the item specified in path parameter.

- Endpoint : http://localhost:5000/list/{item}

- Path Parameters: 
    - item (required) : Entities available: 'character', 'scene', 'season', 'episode'.

- Query Parameters: 
    - season (optional, except for 'scene') : for filtering to a specific season.
    - episode (optional, except for 'scene') : for filtering to a specific episode of a season (This only applies when season query parameter is also specified.)
 

- Response: 
    - On success (example):
```
http://localhost:5000/list/character?season=4
```
```json
[
  "Alice", 
  "All", 
  "Allesandro", 
  "Amanda", 
  "Bonnie", 
  "Both", 
  "Carol", 
  "Casey", 
  "Chandler", 
  "Cheryl", 
  "Chip", 
  "Chloe", 
  "Devon", 
  "Doctor", 
  "Drew", 
  "Emily", 
  "Everyone", 
  "Felicity", 
  "Fergie", 
  "Frank", 
  "Gunther", 
  "Guy", 
  "Housekeeper", 
  "Interviewer", 
  "Janice", 
  "Joanna", 
  "Joey", 
  "Josh", 
  "Joshua", 
  "Julie", 
  "Kathy", 
  "Liam", 
  "Marjorie", 
  "Mike", 
  "Minister", 
  "Minster", 
  "Monica", 
  "Nurse", 
  "Oven", 
  "Passenger", 
  "Peter", 
  "Phoebe", 
  "Rachel", 
  "Rick", 
  "Ross", 
  "Sophie", 
  "Susan", 
  "Tim", 
  "Tony", 
  "Ursula", 
  "Voice", 
  "Waiter", 
  "Woman"
]
```

- 
    - On error (example):
```
http://localhost:5000/list/character?season=11
```

"Error. The season 11 entried does not exist. Please check API documentation for finding available seasons."

## Random Character Script Line

Retrieves a random script line of a specific character.

- Endpoint : http://localhost:5000/line/{character}

- Path Parameters: 
    - character (required) : name of a character

- Response: 
    - On success (example):

```
http://localhost:5000/line/Chandler
```

```json
[
  {
    "line": "So, how many have you sold so far?", 
    "episode": {
      "season": "3", 
      "number": "10", 
      "name": "Rachel Quits"
    }, 
    "scene": {
      "_id": "5fc2847babbba8b12effa06e", 
      "attendees": [
        "Ross", 
        "Chandler", 
        "Monica", 
        "Rachel", 
        "Joey"
      ]
    }
  }
]
```

- 
    - On error (example):
```
http://localhost:5000/line/lkl
```
"Error. The character lkl do not exist. Please check API documentation for finding available characters."



## Retrieve a Scene

Retrieves a whole scene.

- Endpoint : http://localhost:5000/scene/{scene_id}

- Path Parameters: 
    - scene_id (required) : Scene ObjectID. If 'random' is provided, it retreives a random scene.

- Query Parameters: 
    - season (optional) : for filtering to a specific season (This only applies if 'random' scene_id is provided.)
    - episode (optional) : for filtering to a specific episode of a season (This only applies if 'random' scene_id is provided and when season is also specified.)
    - limit (optional, integer): limit number of cases. By default = 1. Max limit = 10. If exceeded, it will return only 10.

- Response: 
    - On success (example):
```
http://localhost:5000/scene/random?season=3&episode=15&limit=2
```
```json
[
  {
    "_id": "5fc2847fabbba8b12effa0b6", 
    "episode": {
      "season": "3", 
      "number": "15", 
      "name": "Ross And Rachel Take A Break"
    }, 
    "attendees": [
      "Chandler", 
      "Issac", 
      "Joey", 
      "Chloe"
    ], 
    "script": [
      {
        "speaker": "Chandler", 
        "line": "Come on Chloe! Finish up with your customer first. Come on Chloe! Come on Chloe!!", 
        "sentiment_score": 0.0
      }, 
      {
        "speaker": "Issac", 
        "line": "Can I help you?", 
        "sentiment_score": 0.4019
      }, 
      {
        "speaker": "Chandler", 
        "line": "Uh-oh.", 
        "sentiment_score": 0.0
      }, 
      {
        "speaker": "Joey", 
        "line": "Uh, y'know what, we’re having second thoughts about our copying needs. And we’ll need a little more time to think about it.", 
        "sentiment_score": 0.0
      }, 
      {
        "speaker": "Issac", 
        "line": "Chloe, switch with me, there’s some guys here that got a crush on you.", 
        "sentiment_score": -0.1531
      }, 
      {
        "speaker": "Chandler", 
        "line": "Okay, that hurt us.", 
        "sentiment_score": -0.3612
      }, 
      {
        "speaker": "Chloe", 
        "line": "Hi guys. I haven’t seen you since this morning.", 
        "sentiment_score": 0.0
      }, 
      {
        "speaker": "Chandler", 
        "line": "Well ah, ........y'know.", 
        "sentiment_score": 0.2732
      }, 
      {
        "speaker": "Chloe", 
        "line": "Hey, what are you guys doing tomorrow night?", 
        "sentiment_score": 0.0
      }, 
      {
        "speaker": "Joey", 
        "line": "Both of us?", 
        "sentiment_score": 0.0
      }, 
      {
        "speaker": "Chloe", 
        "line": "Maybe. Does that scare ya?", 
        "sentiment_score": -0.4939
      }, 
      {
        "speaker": "Chloe", 
        "line": "Relax. It’s just Issac’s D.J.-ing at the Philly. You should come.", 
        "sentiment_score": 0.4404
      }, 
      {
        "speaker": "Joey", 
        "line": "We’ll be there.", 
        "sentiment_score": 0.0
      }, 
      {
        "speaker": "Chloe", 
        "line": "Great. I’ll ah, see ya then.", 
        "sentiment_score": 0.6249
      }, 
      {
        "speaker": "Chandler", 
        "line": "All right, rock on.", 
        "sentiment_score": 0.0
      }
    ]
  }, 
  {
    "_id": "5fc28480abbba8b12effa0c5", 
    "episode": {
      "season": "3", 
      "number": "15", 
      "name": "Ross And Rachel Take A Break"
    }, 
    "attendees": [
      "Sergei", 
      "Phoebe", 
      "Joey"
    ], 
    "script": [
      {
        "speaker": "Sergei", 
        "line": "Touchet, touchet, Miss Americccan pie.  Ameri-ccan.", 
        "sentiment_score": -0.1531
      }, 
      {
        "speaker": "Phoebe", 
        "line": "Ameri-can.", 
        "sentiment_score": 0.0
      }, 
      {
        "speaker": "Sergei", 
        "line": "Ameri-ccan.", 
        "sentiment_score": 0.0
      }, 
      {
        "speaker": "Phoebe", 
        "line": "Ameri-can. Y'know it’s a very hard language. Let’s do it again.", 
        "sentiment_score": -0.1027
      }, 
      {
        "speaker": "Sergei", 
        "line": "Everybody!!", 
        "sentiment_score": 0.0
      }, 
      {
        "speaker": "Joey", 
        "line": "Previously on Friends.", 
        "sentiment_score": 0.4767
      }
    ]
  }
]
```

- 
    - On error (example):
```
http://localhost:5000/scene/random?season=12&limit=2
```

"Error. The season 12 entried does not exist. Please check API documentation for finding available seasons."

## Sentiment Character

Retrieves a character overall sentiment score.

- Endpoint : http://localhost:5000/sentiment/character/{character}

- Path Parameters: 
    - character (required) : name of a character

- Query Parameters: 
    - season (optional) : for filtering to a specific season.
    - episode (optional) : for filtering to a specific episode of a season (This only applies when season query parameter is also specified.)
 

- Response: 
    - On success (example):
```
http://localhost:5000/sentiment/character/Joey?season=5&episode=13
```
```json
[
  {
    "character": "Joey", 
    "sentiment_score": 0.09
  }
]
```

- 
    - On error (example):
```
http://localhost:5000/sentiment/character/dummy_char
```

"Error. The character dummy_char do not exist. Please check API documentation for finding available characters."
## Sentiment Episode

Retrieves an episode overall sentiment score.

- Endpoint : http://localhost:5000/sentiment/episode/

- Query Parameters: 
    - season (required) 
    - episode (required) 
 

- Response: 
    - On success (example):
```
http://localhost:5000/sentiment/episode/?season=3&episode=2
```
```json
[
  {
    "season": "3", 
    "episode": "2", 
    "sentiment_score": 0.08
  }
]
```
- 
    - On error (example):
```
http://localhost:5000/sentiment/episode
```

"Error. Missing a required parameter. Please check API documentation."






