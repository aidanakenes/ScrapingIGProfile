from fastapi import FastAPI, Query
from src.controller import *

app = FastAPI()


@app.get('/profile')
def get(username: str = Query(..., max_length=30, description='Collect data of IG profile')):
    user = get_user_info(username=username)
    return {'user': user}
