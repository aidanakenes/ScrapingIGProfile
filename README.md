 # ObservingInstaProfile

 ### Intro
I am just learning and trying to improve my code skills.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install libraries from requirements.txt file.

```bash
pip install -r requirements.txt
```

## Project
The application is made for observing profiles of the Instagram users: full name, bio info, number of posts, followers and followings, etc.
You can notice functions:

```python

extract_data(username:str) -> dict # extracts profile information in json format via username
get_user_info(username:str) -> User # return object of the user with profile information
save_data(users:list) # save list of users into json file
download_pictures(users:list) # doamload all profile pictures of the users from the provided list
```

In the tests/test.py you can see test-code of these functions

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### THANKS FOR ATTENTION! GOOD LUCK!
