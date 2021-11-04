import pytest

from src.service.parser import IGParser
from src.models.user import User

usernames_to_search = ['google', 'facebook', 'twitter']

username_ids = [f'username: {u}'
                for u in usernames_to_search]


@pytest.mark.parametrize('username', usernames_to_search, ids=username_ids)
def test_parser(username):
    parser = IGParser()
    t_user: User = parser.get_user(username=username)
    assert t_user is not None


usernames_to_validate = [123, True, 3.4]

username_validate_ids = [f'username: {u}'
                         for u in usernames_to_validate]


@pytest.mark.parametrize('username', usernames_to_validate, ids=username_validate_ids)
def test_parser_input(username):
    parser = IGParser()
    with pytest.raises(TypeError):
        parser.get_user(username=username)
