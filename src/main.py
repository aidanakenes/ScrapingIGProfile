from fastapi import FastAPI, Query
from src.controller import *

app = FastAPI()


@app.get('/profile')
def get(username: str = Query(..., description='Collect data of IG profile')):
    return {'info': get_user_info(username=username)}
