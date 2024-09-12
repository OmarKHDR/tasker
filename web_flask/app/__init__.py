from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Conf:
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{basedir}/app/tasker.db"

app = Flask(__name__, static_url_path="/webstatic", static_folder=f"{basedir}/webstatic")
app.config.from_object(Conf)
from app import routes