import os
import random

db_info = {'host': 'localhost',
           'database': 'login',
           'pass': 'fistook22',
           'user': 'postgres',
           'port': ''}


class Config:
    SECRET_KEY = random._urandom(56)
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{db_info['user']}:{db_info['pass']}@{db_info['host']}/{db_info['database']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
