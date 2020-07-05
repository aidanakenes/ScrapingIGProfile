import requests
import json
import logging
from typing import List
from src.models import User

USERS_FILE = '../data/users.json'
PICTURES_DIR = '../data/pictures/'


class IGUserSaver:

    def __init__(self, users_file: str = USERS_FILE, pictures_dir: str = PICTURES_DIR):
        self.users_file = users_file
        self.pictures_dir = pictures_dir

    def save_users(self, users: List[User]) -> None:
        # Todo: Save users in a json file. Use self.users_file
        users = [u.__dict__ for u in users]
        try:
            with open(self.users_file, 'w', encoding='utf-8') as f:
                users = json.dumps(users, indent=4, sort_keys=True, ensure_ascii=False)
                f.write(users)
        except IOError:
            logging.info(f'Failed to save data into {self.users_files}')

    def download_pictures(self, users: List[User]) -> None:
        for user in users:
            r = requests.get(
                url=user.profile_picture_url,
                timeout=10
            )
            if r.ok:
                with open(file=f'{self.pictures_dir}{user.username}.jpg', mode='wb') as f:
                    f.write(r.content)
            else:
                # Todo: Handle Requests, File exceptions
                logging.info(f'{r.text} [{r.status_code}]\n'
                             f'Failed to get picture {user.profile_picture_url} ')


if __name__ == '__main__':
    from pprint import pprint
    from src.parser import IGParser

    parser = IGParser()
    t_user = parser.get_user(username='kazdream_live')
    pprint(t_user.dict())
    saver = IGUserSaver()
    saver.download_pictures(users=[t_user])
