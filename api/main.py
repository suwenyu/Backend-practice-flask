from flask import Blueprint
from flask_restplus import Api

from api.controller.auth_controller import api as auth_ns
from api.controller.message_controller import api as message_ns
from api.controller.post_controller import api as post_ns
from api.controller.user_controller import api as user_ns

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="FLASK RESTPLUS API BOILER-PLATE WITH JWT",
    version="1.0",
    description="a boilerplate for flask restplus web service",
)

api.add_namespace(user_ns, path="/user")
api.add_namespace(auth_ns)
api.add_namespace(post_ns, path="/post")
api.add_namespace(message_ns, path="/message")
