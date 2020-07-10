import re
import json
import requests
from typing import Optional
from src.models import User
from src.err_utils import *


class IGParser:

    def __init__(self):
        self.ig_home = 'https://www.instagram.com/'

    def get_user(self, username: str) -> Optional[User]:
        r = requests.get(
            url=f'{self.ig_home}{username}',
            timeout=10
        )
        if r.ok:
            regex = r'(?<="graphql":{"user":).*(?=},"toast_)'
            try:
                regex_res = re.findall(pattern=regex, string=r.text)[0]
                _user = json.loads(regex_res)
                return User(
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
            except Exception:
                raise RegexError()
        else:
            return None
