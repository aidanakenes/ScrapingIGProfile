import requests, json, re, ast
from pydantic import BaseModel, ValidationError
import logging

FILE_SAVE_PATH = 'C:/Users/Lenovo/PycharmProjects/ObservingInstagramProfile/data/'


class User(BaseModel):
    username: str
    fullname: str = None
    id: str
    url: str = None
    bio: str = None
    followers: int
    followings: int
    profile_picture_url: str = None
    is_business: bool


def download_pictures(users: list):
    for user in users:
        try:
            pic_url = user['profile_picture_url']
            response = requests.get(pic_url, verify=False)
            with open(FILE_SAVE_PATH + pic_url[18:35] + '.jpg', 'wb') as f:
                f.write(response.content)
            response.raise_for_status()
        except Exception as e:
            logging.error(f'Exception: {e}\n Couldn\'t save picture {pic_url}')

    logging.info('Pictures were installed successfully')


def save_data(users: list):
    try:
        file_path = FILE_SAVE_PATH + 'insta_data.json'
        with open(FILE_SAVE_PATH + file_name, 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=4, sort_keys=True, ensure_ascii=False)
    except Exception as e:
        logging.error(f'Exception: {e}\n Couldn\'t save data into {file_path}')
    else:
        logging.info(f'Data was saved successfully into {file_path}')


def extract_data(username: str) -> dict:
    profile_url = 'https://www.instagram.com/' + username + '/'
    try:
        response = requests.get(profile_url, verify=False)
        html_page = response.text
        regex = r'(?<="graphql":).*(?=,"toast_)'
        json_data = json.loads(re.findall(regex, html_page)[0])['user']
    except requests.ConnectionError as e:
        logging.error(f'Connection Error: failed to connect with {profile_url}')

    return json_data


def get_user_info(username: str) -> User:
    json_data = extract_data(username)

    try:
        return User(
            username=username,
            fullname=json_data['full_name'],
            id=json_data['id'],
            url=json_data['external_url'],
            bio=json_data['biography'],
            followers=json_data['edge_followed_by']['count'],
            followings=json_data['edge_follow']['count'],
            profile_picture_url=json_data['profile_pic_url_hd'],
            is_business=json_data['is_business_account']
        )
    except ValidationError as e:
        logging.error(f'Validation Error: {e.json()}')

    return None


if __name__ == '__main__':
    pass
