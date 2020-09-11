import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphene_sqlalchemy import SQLAlchemyObjectType

from api.schema.post import PostGraphSchema
from api.schema.user import UserGraphSchema


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_users = SQLAlchemyConnectionField(UserGraphSchema.connection)
    # Disable sorting over this field
    all_posts = SQLAlchemyConnectionField(
        PostGraphSchema.connection, sort=None)


schema = graphene.Schema(query=Query)
