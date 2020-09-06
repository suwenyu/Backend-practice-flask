from marshmallow import ValidationError

from api.generics import GenericAPIView
from api.model.user import Post


class PostView(GenericAPIView):
    model = Post
