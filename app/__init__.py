from flask import Flask

from flask.ext.login import LoginManager
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = '/'

app = Flask(__name__)

from config import *

from models import db
db.init_app(app)

from app import views

login_manager.init_app(app)