import re
from typing import Union
from src.err_utils import ApplicationError
from src.parser import IGParser
from src.models import User


def check_username(username: str) -> Union[bool, ApplicationError]:
    if len(username) > 30:
        return ApplicationError(
            message='Invalid username: length of username must be less than 30',
            status_code=400
        )
    regex = '[^A-Za-z0-9_.]'
    regex_res = re.compile(pattern=regex)
    invalid = regex_res.search(username)
    if invalid:
        return ApplicationError(
            message='Invalid username: username can contain only letters, numbers, periods and underscores',
            status_code=400
        )
    return True


def get_user_info(username: str) -> Union[User, ApplicationError]:
    validation = check_username(username=username)
    if isinstance(validation, ApplicationError):
        return validation
    if validation:
        parser = IGParser()
        user = parser.get_user(username=username)
        return user
