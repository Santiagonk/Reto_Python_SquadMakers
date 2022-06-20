from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import dotenv_values

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    config = dotenv_values(".env")
    app.config['SQLALCHEMY_DATABASE_URI'] = config['DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .main import main
    app.register_blueprint(main)

    from .jokes import jokes
    app.register_blueprint(jokes)

    from .math import math
    app.register_blueprint(math)

    return app