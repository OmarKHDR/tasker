from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))
class Conf:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{basedir}/tasker.db"

app = Flask(__name__, static_url_path="/webstatic", static_folder=f"{basedir}/webstatic")
app.config.from_object(Conf)
login = LoginManager(app)
login.login_view = 'login'
db = SQLAlchemy(app)
from app import routes