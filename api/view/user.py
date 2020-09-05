from marshmallow import ValidationError

from api.generics import GenericAPIView
from api.model.user import User


class UserView(GenericAPIView):
    model = User

    def create(self, data):
        try:
            obj = self.schema.load(data)
            self.perform_create(obj)

            return self.generate_token(obj)

        except ValidationError as err:
            print(err.messages)

    def generate_token(self, user):
        try:
            # generate the auth token
            auth_token = user.encode_auth_token(user.id)
            response_object = {
                'status': 'success',
                'message': 'Successfully registered.',
                'Authorization': auth_token.decode(),
                'data': self.schema.dump(user)
            }
            return response_object, 201

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return response_object, 401
