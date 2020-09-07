from flask_restplus import fields
from flask_restplus import Namespace
from flask_restplus import reqparse


class UserDto:

    api = Namespace("user", description="user related operations")
    user = api.model(
        "user",
        {
            "email": fields.String(required=True, description="user email address"),
            "username": fields.String(required=True, description="user username"),
            "password": fields.String(required=True, description="user password"),
            "public_id": fields.String(description="user Identifier"),
        },
    )


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class PostDto:
    api = Namespace("post", description="post related operations")
    post = api.model(
        "post",
        {
            "title": fields.String(required=True, description="post title"),
            "content": fields.String(request=True, description="post content"),
        }
    )
    parser = reqparse.RequestParser()
    parser.add_argument('user_id', type=int, help='get user all posts')


class MessageDto:
    api = Namespace("message", description="message related operations")
    message = api.model(
        "message",
        {
            "message": fields.String(description="message")
        }
    )
