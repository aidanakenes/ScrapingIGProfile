def get_usernames() -> list:
    # Todo: Read the usernames from data/usernames.txt and return a list of usernames
    with open('../data/usernames.txt', 'r') as f:
        usernames = f.read().split()
    return usernames


def collect_all(usernames: list) -> None:
    # Todo: using IGParser and IGUserSaver, collect and save all users for the given usernames
    from src.parser import IGParser
    from src.saver import IGUserSaver
    parser = IGParser()
    users = [parser.get_user(username=username) for username in usernames]
    saver = IGUserSaver()
    saver.save_users(users=users)
    saver.download_pictures(users=users)


if __name__ == '__main__':
    collect_all(usernames=get_usernames())
