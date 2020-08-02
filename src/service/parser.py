import re
import json

import requests
from typing import Optional

from src.models.models import User
from src.utils.err_utils import *
from src.utils.logger import get_logger

logger = get_logger(__name__)


class IGParser:

    def __init__(self):
        self.ig_home = 'https://www.instagram.com/'

    def get_user(self, username: str) -> Optional[User]:
        try:
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
                    logger.info(f"Returning the IGParser's result for username {username}")
                    return user
        except TimeoutError as e:
            logger.error(f'Cannot parse page for {username}: {type(e)}')
            raise ApplicationError()
        except Exception as e:
            logger.error(f'Cannot parse page for {username}: {type(e)}')
            raise RegexError()
