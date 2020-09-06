from api import db
from api.model.base import Base


class Post(Base):
    """ Post Model for storing user's post related details """

    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text)
