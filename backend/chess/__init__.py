from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
users = {}
scores = {}

auth = HTTPBasicAuth()
from . import routes

