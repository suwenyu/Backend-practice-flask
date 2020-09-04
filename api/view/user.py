from flask_restplus import reqparse

from api.generics import GenericAPIView
from api.model.user import User


class UserView(GenericAPIView):
    model = User
