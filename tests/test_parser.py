from src.parser import IGParser
from src.models import User


def test_parser():
    parser = IGParser()
    t_user: User = parser.get_user(username='zhvnibeek')
    assert t_user is not None
