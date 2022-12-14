from flask import Flask
from flask_httpauth import HTTPBasicAuth

def create_app(env = None):
    app = Flask(__name__, instance_relative_config=False)
    users = {}
    scores = {}

    auth = HTTPBasicAuth()
    from . import routes
    routes.configure_routes(app, auth, users, scores)

    return app

