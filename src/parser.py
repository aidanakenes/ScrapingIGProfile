import re
import json
import requests
import logging
from typing import Optional
from src.models import User


class IGParser:

    def __init__(self):
        self.ig_home = 'https://www.instagram.com/'

    def get_user(self, username: str) -> Optional[User]:
        r = requests.get(
            url=f'{self.ig_home}{username}',
            timeout=10  # always set timeout
        )
        if r.ok:
            regex = r'(?<="graphql":).*(?=,"toast_)'
            _user = json.loads(re.findall(pattern=regex, string=r.text)[0])['user']
            # Todo: What exception could be raised here?
            if _user:
                return User(
                    id=_user.get('id'),  # Use .get('key') instead ['key']
                    url=f'{self.ig_home}{username}',
                    bio=_user.get('biography'),
                    username=username,
                    fullname=_user['full_name'],
                    followers=_user.get('edge_followed_by', {}).get('count'),
                    followings=_user.get('edge_follow', {}).get('count'),
                    is_business=_user.get('is_business_account'),
                    is_private=_user.get('is_private'),
                    profile_picture_url=_user.get('profile_pic_url_hd')
                )
            else:
                logging.info(f'RegEx Error: Failed to get data from {username}')
        else:
            # Todo: handle exception properly. Log response status code, response text
            logging.info(f'{r.text} [{r.status_code}]\n'
                         f'Failed to get page for {username} ')


if __name__ == '__main__':
    from pprint import pprint

    parser = IGParser()
    t_user: User = parser.get_user(username='kazdream_live')
    pprint(t_user.dict())
