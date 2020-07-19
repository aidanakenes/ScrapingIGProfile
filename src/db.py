from pymongo import MongoClient
from src.conf import MongoConfig
from src.models import User

client = MongoClient(**MongoConfig)
my_db = client['my_db']
users_collection = my_db['ig_users']


def insert_user_db(_user: User):
    print(f"Saving the result into database for username {_user.username}")
    users_collection.update({'id': _user.id}, _user.dict(), upsert=True)
