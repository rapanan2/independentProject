import os
import sqlalchemy
from flask import Flask
from yaml import load, Loader
from config import Config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)

Bootstrap(app)