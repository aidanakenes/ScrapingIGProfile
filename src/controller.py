import re
import logging
from src.parser import IGParser
from src.models import User


def check_username(username: str) -> bool:
    if len(username) >= 30:
        logging.error('Invalid username: can contain only letters, numbers, periods and underscores')
        return False
    regex = '[^A-Za-z0-9_.]'
    re_res = re.compile(pattern=regex)
    invalid = re_res.search(username)
    if invalid:
        logging.error('Invalid username: length of username must be less than 30')
        return False
    return True


def get_user_info(username: str) -> User:
    if check_username(username=username):
        parser = IGParser()
        user = parser.get_user(username=username)
        return user

