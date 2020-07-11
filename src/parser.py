import re
import json
import requests
import hashlib
import redis
import ast
from typing import Optional
from src.models import User
from src.err_utils import *


class IGParser:

    def __init__(self):
        self.ig_home = 'https://www.instagram.com/'
        self.rds = redis.Redis(host='127.0.0.1', port=6379)

    def get_user(self, username: str) -> Optional[User]:
        hash = hashlib.md5(str.encode(username))
        hash_key = hash.hexdigest()
        _user = self.rds.get(name=hash_key)

        if _user is None:
            r = requests.get(
                url=f'{self.ig_home}{username}',
                timeout=10
            )
            if r.ok:
                regex = r'(?<="graphql":{"user":).*(?=},"toast_)'
                try:
                    regex_res = re.findall(pattern=regex, string=r.text)[0]
                    _user = json.loads(regex_res)
                    user = User(
                        id=_user.get('id'),
                        url=f'{self.ig_home}{username}',
                        bio=_user.get('biography'),
                        username=username,
                        fullname=_user.get('full_name'),
                        followers=_user.get('edge_followed_by', {}).get('count'),
                        followings=_user.get('edge_follow', {}).get('count'),
                        is_business=_user.get('is_business_account'),
                        is_private=_user.get('is_private'),
                        profile_picture_url=_user.get('profile_pic_url_hd')
                    )
                    self.rds.set(name=hash_key, value=str(user.dict()))
                    return user
                except ValueError:
                    raise RegexError()
            else:
                return None
        else:
            u = ast.literal_eval(_user.decode('utf-8').replace("'", "\""))
            return User(**u)
