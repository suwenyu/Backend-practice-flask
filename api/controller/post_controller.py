from flask import request
from flask_jwt_extended import jwt_required
from flask_restplus import reqparse
from flask_restplus import Resource

from api.model.post import Post as PostModel
from api.schema.post import PostSchema
from api.service.auth_helper import Auth
from api.util.decorator import token_required
from api.util.dto import PostDto
from api.view.post import PostView

api = PostDto.api
_post = PostDto.post
parser = PostDto.parser


@api.route("/")
class UserList(Resource, PostView):
    model = PostModel

    @api.doc("list_of_post_from_user")
    @api.marshal_list_with(_post, envelope="data")
    @api.expect(parser, validate=True)
    def get(self):
        """List all posts from user"""
        self.schema = PostSchema(many=True)
        args = parser.parse_args()
        user_id = args['user_id']
        self.queryset = self.model.query.filter_by(user_id=user_id)
        return self.list()

    @api.response(201, "Post successfully created.")
    @api.doc("create a new post")
    @api.expect(_post, validate=True)
    @jwt_required
    def post(self):
        """Creates a new User """
        self.schema = PostSchema()
        data = request.json
        user_data, status_code = Auth.get_logged_in_user(request)
        data['user_id'] = user_data['data']['user_id']

        return self.create(data)


@api.route("/<id>")
@api.response(404, "Post not found.")
class UserDetail(Resource, PostView):
    model = PostModel
    schema = PostSchema()

    @api.doc("get a post")
    @api.marshal_with(_post)
    def get(self, id):
        """get a post given its identifier"""
        self.queryset = self.model.query.filter_by(id=id).first()
        return self.retrieve()

    @api.doc("update a post")
    @api.marshal_with(_post)
    @api.expect(_post, validate=True)
    @jwt_required
    def put(self, id):
        """update a user given its identifier """

        data = request.json
        user_data, status_code = Auth.get_logged_in_user(request)
        user_id = user_data['data']['user_id']
        data['user_id'] = user_id

        self.queryset = self.model.query.filter_by(
            id=id, user_id=user_id).first()
        return self.update(data)

    @api.doc("delete a post")
    @jwt_required
    def delete(self, id):
        """delete a user given its identifier """
        user_data, status_code = Auth.get_logged_in_user(request)
        user_id = user_data['data']['user_id']
        self.queryset = self.model.query.filter_by(
            id=id, user_id=user_id).first()
        return self.destroy()
