import os

appAbsolutePath = os.path.dirname(__file__)


class Config:
    SECRET_KEY = "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{appAbsolutePath}/users.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
