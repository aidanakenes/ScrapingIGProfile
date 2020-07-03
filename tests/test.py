import requests, json
import re, ast
from src import*

def test1():
    try:
        with open('usernames.txt', 'r') as f:
            text = f.read()
            usernames = ast.literal_eval(text)
        usernames_to_save = list()

    except Exception as e:
        raise SystemExit(f'{e}')

    for u in usernames:
        user = get_user_info(u)
        download_picture(user[u]['profile_pic_url_hd'])
        usernames_to_save.append(user)

    save_data(usernames_to_save)