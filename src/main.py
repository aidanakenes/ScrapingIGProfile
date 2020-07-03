import requests, json
import re, ast

FILE_SAVE_PATH = 'C:/Users/Lenovo/PycharmProjects/data/'


def download_picture(picture_url: str):
    try:
        response = requests.get(picture_url, verify=False)
        with open(FILE_SAVE_PATH + picture_url[18:35] + '.jpg', 'wb') as f:
            f.write(response.content)
        r.raise_for_status()

    except IOError:
        print(f'Could not read file: {f.name}')
    except requests.exceptions.HTTPError as e:
        raise SystemExit(err)
    except Exception as e:
        raise SystemExit(f'Cannot extract data from url: {e}')
    else:
        print('Picture was installed successfully ')


def get_user_info(username: str) -> dict:
    profile_url = 'https://www.instagram.com/' + username + '/'

    try:
        response = requests.get(profile_url, verify=False)
        html_page = response.text
        regex = r'(?<="graphql":).*(?=,"toast_)'
        json_data = dict()
        json_data[username] = json.loads(re.findall(regex, html_page)[0])
        r.raise_for_status()

    except ValueError as e:
        raise SystemExit(f'ValueError: {f.name}')
    except requests.exceptions.HTTPError as e:
        raise SystemExit(err)
    except Exception as e:
        raise SystemExit(f'Cannot extract data from url: {e}')

    try:
        user = {
            username:
                {
                    'biography': json_data[username]['user']['biography'],
                    'external_url': json_data[username]['user']['external_url'],
                    'edge_followed_by': json_data[username]['user']['edge_followed_by'],
                    'edge_follow': json_data[username]['user']['edge_follow'],
                    'id': json_data[username]['user']['id'],
                    'is_business_account': json_data[username]['user']['is_business_account'],
                    'full_name': json_data[username]['user']['full_name'],
                    'profile_pic_url_hd': json_data[username]['user']['profile_pic_url_hd']
                }
        }
    except ValueError as e:
        raise SystemExit(f'ValueError: {f.name}')
    except Exception as e:
        raise SystemExit(f'Cannot get user data: {e}')

    return user


def save_data(user: list):
    try:
        with open(FILE_SAVE_PATH + 'insta_data.json', 'w', encoding='utf-8') as f:
            json.dump(user, f, indent=4, sort_keys=True, ensure_ascii=False)

    except IOError:
        raise SystemExit(f'Could not read file: {f.name}')
    except Exception as e:
        raise SystemExit(f'Cannot insert data into json file: {e}')
    else:
        print('Data was installed successfully')


if __name__ == '__main__':
    pass
