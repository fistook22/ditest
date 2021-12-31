from flask import Flask

from app.config import Config

app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)
