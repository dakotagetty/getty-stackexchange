from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
requested_users = 20

from app import routes