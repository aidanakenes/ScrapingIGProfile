import redis
import hashlib
import ast
from typing import Optional
from src.models import User

class Cache:

    def __init__(self):
        self.caches = redis.Redis(host='127.0.0.1', port=6379)

    def get(self, username: str) -> Optional[User]:
        hash = hashlib.md5(str.encode(username))
        hash_key = hash.hexdigest()
        _user = self.caches.get(name=hash_key)
        if _user:
            u = ast.literal_eval(_user.decode('utf-8').replace("'", "\""))
            return User(**u)

    def save_cache(self, user:User):
        try:
            hash = hashlib.md5(str.encode(user.username))
            hash_key = hash.hexdigest()
            self.caches.set(name=hash_key, value=str(user.dict()))
        except ConnectionError as e:
            raise e

