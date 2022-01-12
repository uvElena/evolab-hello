from flask import Flask
from models import db


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    return app


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../state/names.db'
