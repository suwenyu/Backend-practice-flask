from flask import request
from flask_restplus import Resource

from api.model.user import User as UserModel
from api.schema.user import UserSchema
from api.util.dto import UserDto
from api.view.user import UserView


api = UserDto.api
_user = UserDto.user


@api.route("/")
class UserList(Resource, UserView):
    model = UserModel

    @api.doc("list_of_registered_users")
    @api.marshal_list_with(_user, envelope="data")
    def get(self):
        """List all registered users"""
        self.schema = UserSchema(many=True)
        self.queryset = self.model.query.all()
        return self.list()

    @api.response(201, "User successfully created.")
    @api.doc("create a new user")
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        self.schema = UserSchema()
        data = request.json
        return self.create(data)


@api.route("/<id>")
@api.response(404, "User not found.")
class UserDetail(Resource, UserView):
    model = UserModel
    schema = UserSchema()

    @api.doc("get a user")
    @api.marshal_with(_user)
    def get(self, id):
        """get a user given its identifier"""
        self.queryset = self.model.query.filter_by(id=id).first()
        return self.retrieve()

    @api.doc("update a user")
    @api.marshal_with(_user)
    @api.expect(_user, validate=True)
    def put(self, id):
        """update a user given its identifier """
        self.queryset = self.model.query.filter_by(id=id)
        data = request.json
        data.pop("password")
        print(data)
        return self.update(data)

    @api.doc("delete a user")
    def delete(self, id):
        """delete a user given its identifier """
        self.queryset = self.model.query.filter_by(id=id).first()
        return self.destroy()
