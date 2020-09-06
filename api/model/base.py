from datetime import datetime
from datetime import timedelta

from api import db
from api import flask_bcrypt
from config import key


class Base(db.Model):
    __abstract__ = True

    created_on = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_on = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )
