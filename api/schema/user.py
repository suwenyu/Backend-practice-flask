from marshmallow import fields

from api import ma
from api.model.user import User as UserModel


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        exclude = ("password_hash",)
        load_instance = True

    password = fields.Str(load_only=True)
