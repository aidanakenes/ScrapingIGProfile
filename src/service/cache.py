import json

import redis

from src.service.conf import RedisConfig
from src.models.models import User
from src.utils.logger import get_logger
from src.service.conf import REDIS_TTL

logger = get_logger(__name__)


class Cache:

    def __init__(self):
        self.my_redis = redis.Redis(**RedisConfig)

    def get_cache(self, username: str):
        logger.info(f"Returning the cached result for username {username}")
        cached = self.my_redis.get(username)
        if cached is not None:
            return User(**json.loads(cached))

    def save_cache(self, user: User):
        logger.info(f"Caching the result for username {user.username}")
        self.my_redis.setex(
            name=user.username,
            time=REDIS_TTL,
            value=user.json()
        )
