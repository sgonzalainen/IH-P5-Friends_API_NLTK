import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()

DBURL = os.getenv('URL')

if not (DBURL):
    raise ValueError('Tienes que especificar una URL')

client = MongoClient(DBURL)
db =client.get_database()
collection = db['dialogues']