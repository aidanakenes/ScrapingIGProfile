import re
from typing import Union
from src.err_utils import ApplicationError
from http import HTTPStatus
from src.parser import IGParser
from src.models import User


def check_username(username: str) -> ApplicationError:
    if username=='':
        return ApplicationError(
            message='Empty value',
            status_code=HTTPStatus.BAD_REQUEST
        )
    if len(username) > 30:
        return ApplicationError(
            message=f'Invalid username: length of username is {len(username)} (must be less than 30)',
            status_code=HTTPStatus.BAD_REQUEST
        )
    regex = '[^A-Za-z0-9_.]'
    regex_res = re.compile(pattern=regex)
    invalid = regex_res.search(username)
    if invalid:
        return ApplicationError(
            message='Invalid username: username can contain only letters, numbers, periods and underscores',
            status_code=HTTPStatus.BAD_REQUEST
        )


def get_user_info(username: str) -> Union[User, ApplicationError]:
    validation = check_username(username=username)
    if isinstance(validation, ApplicationError):
        return validation
    parser = IGParser()
    _user = parser.get_user(username=username)
    return _user
