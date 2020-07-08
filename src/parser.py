import re
import json
import requests
from http import HTTPStatus
from typing import Union
from src.models import User
from src.err_utils import ApplicationError


class IGParser:

    def __init__(self):
        self.ig_home = 'https://www.instagram.com/'

    def get_user(self, username: str) -> Union[User, ApplicationError]:
        r = requests.get(
            url=f'{self.ig_home}{username}',
            timeout=10
        )
        if r.ok:
            regex = r'(?<="graphql":).*(?=,"toast_)'
            regex_res = re.findall(pattern=regex, string=r.text)[0]
            if regex_res:
                _user = json.loads(regex_res)['user']
                return User(
                    id=_user.get('id'),
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
                return ApplicationError(
                    message=f'RegEx Error: Invalid Regex',
                    status_code=HTTPStatus.BAD_REQUEST
                )
        else:
            return ApplicationError(
                message=f'Failed to get page for {username} ',
                status_code=r.status_code
            )


