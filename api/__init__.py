from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_cors import cross_origin
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

from config import config_by_name


db = SQLAlchemy()
ma = Marshmallow()

flask_bcrypt = Bcrypt()

cors = CORS()
socketio = SocketIO(cors_allowed_origins="*")

jwt = JWTManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)

    flask_bcrypt.init_app(app)
    ma.init_app(app)
    socketio.init_app(app)

    cors.init_app(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    jwt.init_app(app)

    return app
