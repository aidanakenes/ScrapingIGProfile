import src

def test():
    usernames = list()
    try:
        with open('usernames.txt', 'r') as f:
            text = f.read()
            usernames = ast.literal_eval(text)

    except Exception as e:
        logging.error(f'{e}')

    users = [get_user_info(username).dict() for username in usernames]
    print(users)
    download_pictures(users)
    save_data(users)
