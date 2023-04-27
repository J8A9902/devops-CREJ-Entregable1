from flask import Flask

from helpers.extensions import register_blueprints, initialize_database

application: Flask = Flask(__name__)


with application.app_context():
    initialize_database(application)
    register_blueprints(application)
