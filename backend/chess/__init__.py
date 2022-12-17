from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from passlib.hash import argon2

app = Flask(__name__)
app.config.from_prefixed_env()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
password_hasher = argon2

db_url = app.config['SQLALCHEMY_DATABASE_URI']
if db_url.startswith('sqlite'):
    import chess.models
    with app.app_context():
        db.create_all()

auth = HTTPBasicAuth()
from . import models
from . import routes
