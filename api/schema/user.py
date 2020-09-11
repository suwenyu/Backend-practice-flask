import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphene_sqlalchemy import SQLAlchemyObjectType
from marshmallow import fields

from api import ma
from api.model.user import User as UserModel


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        exclude = ("password_hash",)
        load_instance = True

    password = fields.Str(load_only=True)


class UserGraphSchema(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )
