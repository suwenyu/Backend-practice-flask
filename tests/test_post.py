import json
import unittest

from tests.base import BaseTestCase


def register_user(self):
    return self.client.post(
        '/user/',
        data=json.dumps(dict(
            email='test@gmail.com',
            username='test',
            password='123456',
            public_id="test"
        )),
        content_type='application/json'
    )


def login_user(self):
    return self.client.post(
        '/auth/login',
        data=json.dumps(dict(
            email='test@gmail.com',
            password='123456'
        )),
        content_type='application/json'
    )


def add_post(self, login_response):
    if login_response:
        return self.client.post(
            '/post/',
            headers=dict(
                Authorization='Bearer ' + json.loads(
                    login_response.data.decode()
                )['Authorization']
            ),
            data=json.dumps(dict(
                title='test title',
                content='say something'
            )),
            content_type='application/json'
        )
    else:
        return self.client.post(
            '/post/',
            data=json.dumps(dict(
                title='test title',
                content='test content'
            )),
            content_type='application/json'
        )


class TestPostBlueprint(BaseTestCase):

    def test_user_add_post(self):
        """ Test for user create post """
        with self.client:
            # user registration
            user_response = register_user(self)
            response_data = json.loads(user_response.data.decode())
            self.assertTrue(response_data['Authorization'])
            self.assertEqual(user_response.status_code, 201)

            # registered user login
            login_response = login_user(self)
            data = json.loads(login_response.data.decode())

            self.assertTrue(data['Authorization'])
            self.assertEqual(login_response.status_code, 200)
            post_response = add_post(self, login_response)

            self.assertEqual(post_response.status_code, 201)
            response_data = json.loads(post_response.data.decode())
            self.assertTrue(isinstance(response_data['id'], int))

    def test_not_user_add_post(self):
        """ Test for user without login create post """
        with self.client:
            post_response = add_post(self, None)
            self.assertEqual(post_response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
