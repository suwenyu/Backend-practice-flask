import datetime
import unittest

from api import db
from api.model.user import User
from tests.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def test_encode_auth_token(self):
        user = User(
            username="test",
            email='test@test.com',
            password='test',
            public_id="test"
        )
        db.session.add(user)
        db.session.commit()

    def test_decode_auth_token(self):
        user = User(
            username="test",
            email='test@test.com',
            password='test',
            public_id="test"
        )
        db.session.add(user)
        db.session.commit()


if __name__ == '__main__':
    unittest.main()
