from fastapi import FastAPI
from src.service import *

app = FastAPI()


@app.get(
    '/profile',
    description='Get profile info'
)
def get(username: str):
    return get_user_info(username=username)
