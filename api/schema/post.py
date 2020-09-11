import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphene_sqlalchemy import SQLAlchemyObjectType
from marshmallow import fields

from api import ma
from api.model.post import Post as PostModel


class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PostModel
        load_instance = True

    user_id = fields.Int(load_only=True)


class PostGraphSchema(SQLAlchemyObjectType):
    class Meta:
        model = PostModel
        interfaces = (relay.Node, )
