from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import decode_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_refresh_token_required

from api.model.user import User as UserModel


class Auth:
    @staticmethod
    def login_user(data):
        email = data.get("email")
        password = data.get("password")
        try:
            user = UserModel.query.filter_by(email=email).first()
            if user and user.check_password(password):
                response_object = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'Authorization': create_access_token(
                        identity=user.username),
                    'refresh_token': create_refresh_token(
                        identity=user.username)}
                return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = get_jwt_identity()
            # mark the token as blacklisted
            if resp:
                return {
                    'status': 'success',
                    'message': 'log out'
                }, 200
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        data = new_request.headers.get('Authorization')
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            # resp = UserModel.decode_auth_token(auth_token)
            resp = get_jwt_identity()
            user = UserModel.query.filter_by(username=resp).first()
            response_object = {
                'status': 'success',
                'data': {
                    'user_id': user.id,
                    'email': user.email,
                    'admin': user.admin,
                    'created_on': str(user.created_on)
                }
            }
            return response_object, 200
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401
