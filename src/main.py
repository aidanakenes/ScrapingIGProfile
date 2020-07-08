from fastapi import FastAPI, Query
from src.controller import *
from src.err_utils import ApplicationError

app = FastAPI()


@app.get('/profile')
def get(username: str = Query(..., description='Collect data of IG profile')):
    user = get_user_info(username=username)
    if isinstance(user, ApplicationError):
        return {'error':user}
    return {'info': user}
