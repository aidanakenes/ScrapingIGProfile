from pymongo import MongoClient

from src.service.conf import MongoConfig
from src.models.models import User
from src.utils.logger import get_logger

logger = get_logger(__name__)


class DB:
    def __init__(self):
        client = MongoClient(**MongoConfig)
        self._my_db = client['my_db']
        self._users_collection = self._my_db['ig_users']

    def insert_user(self, user: User):
        logger.info(f"Saving the result into database for username {user.username}")
        self._users_collection.update({'id': user.id}, user.dict(), upsert=True)
