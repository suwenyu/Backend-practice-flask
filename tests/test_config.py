import os
import unittest

from flask import current_app
from flask_testing import TestCase

from config import basedir
from manage import app

postgres_local_base = os.environ["DATABASE_URL"]
postgres_test_base = os.environ["DATABASE_URL_TEST"]


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object("config.DevelopmentConfig")
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config["SECRET_KEY"] == "my_precious")
        self.assertTrue(app.config["DEBUG"])
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config["SQLALCHEMY_DATABASE_URI"] == postgres_local_base)


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object("config.TestingConfig")
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config["SECRET_KEY"] == "my_precious")
        self.assertTrue(app.config["DEBUG"])
        self.assertTrue(
            app.config["SQLALCHEMY_DATABASE_URI"] == postgres_test_base)


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object("config.ProductionConfig")
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config["DEBUG"] is False)


if __name__ == "__main__":
    unittest.main()
