from functools import wraps

from flask import request

from api.service.auth_helper import Auth


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        user_data = data.get('data')

        if not user_data:
            return user_data, status

        return f(*args, **kwargs)

    return decorated