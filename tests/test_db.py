import pytest

from src.db.db import DB
from src.models.user import User


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    pass

