from pymongo import MongoClient
from src.conf import MongoConfig
from src.models import User

client = MongoClient(**MongoConfig)
my_db = client['my_db']
users_collection = my_db['ig_users']


def insert_user_db(user: User):
    users_collection.update({'id': user.id}, user.dict(), upsert=True)
