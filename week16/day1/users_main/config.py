import os

appAbsolutePath = os.path.dirname(__file__)

db_info = {'host': 'localhost',
		   'database': 'login',
		   'user': 'postgres',
		   'port': ''}


class Config:
	SECRET_KEY = os.getenv("SECRET")
	SQLALCHEMY_DATABASE_URI = f"postgresql://{db_info['user']}@{db_info['host']}/{db_info['database']}"
	SQLALCHEMY_TRACK_MODIFICATIONS = False
