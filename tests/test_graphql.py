import os
import unittest

from flask import current_app
from graphene.test import Client
from snapshottest import TestCase

from api.schema import schema
from config import basedir
from manage import app


class APITestCase(TestCase):
    def test_graphql_all_users(self):
        """Testing the API for all users"""
        client = Client(schema)
        self.assertMatchSnapshot(client.execute('''{ allUsers }'''))

    def test_graphql_all_posts(self):
        """ Testing the API for all posts """
        client = Client(schema)
        self.assertMatchSnapshot(client.execute(''' { allPosts } '''))


if __name__ == "__main__":
    unittest.main()
