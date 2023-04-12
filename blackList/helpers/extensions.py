from datetime import timedelta
from flask import Flask
import os
from controllers.blackList_controller import trayecto as trayecto1
from config import *
from database import db
from models import *

def initialize_database(app: Flask) -> None:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///test.db")
    print('----------------------------')
    print(app.config["SQLALCHEMY_DATABASE_URI"])
    db.init_app(app)
    db.create_all()

def register_blueprints(app: Flask) -> None:
    app.register_blueprint(trayecto1)
    