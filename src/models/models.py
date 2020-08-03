from pydantic import BaseModel


class User(BaseModel):
    id: str
    url: str
    bio: str
    username: str
    fullname: str
    followers: int
    followings: int
    is_business: bool
    is_private: bool
    profile_picture_url: str
