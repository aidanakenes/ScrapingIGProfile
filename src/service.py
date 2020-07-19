import redis
import json
from src.parser import IGParser
from src.db import *
from src.err_utils import ApplicationError
from src.models import User
from src.conf import RedisConfig


my_redis = redis.Redis(**RedisConfig)


def get_cache(username: str):
    print(f"Returning the cached result for username {username}")
    cached = my_redis.get(username)
    if cached is not None:
        return User(**json.loads(cached))


def save_cache(_user: User):
    print(f"Caching the result for username {_user.username}")
    my_redis.setex(
        name=_user.username,
        time=3600,
        value=_user.json()
    )


def get_user(username: str):
    try:
        parser = IGParser()
        _user: User = parser.get_user(username=username)
        if _user:
            save_cache(_user)
            insert_user_db(_user)
        print(f"Returning the IGParser's result for username {username}")
        return _user
    except ApplicationError as e:
        raise e
