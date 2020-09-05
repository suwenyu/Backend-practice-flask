from flask import jsonify
from flask import request
from flask_restplus import Resource
from marshmallow import ValidationError

from api import db
from utils.exceptions import *


class CreateMixin:
    """
    Create a model instance.
    """

    def create(self, data):
        try:
            obj = self.schema.load(data)
            self.perform_create(obj)
        except ValidationError as err:
            print(err.messages)
        return self.schema.dump(obj), 201

    def perform_create(self, data):
        db.session.add(data)
        db.session.commit()


class UpdateMixin:
    """
    Update a model instance.
    """

    def update(self, data):
        instance = self.get_queryset()
        if instance:
            self.perform_update(data, instance)
            return instance, 201
        else:
            return {"status": "Not found"}, 400

    def perform_update(self, data, instance):
        for k, v in data.items():
            setattr(instance, k, v)
        db.session.commit()


class DestroyMixin:
    """
    Destroy a model instance.
    """

    def destroy(self):
        instance = self.get_queryset()
        # instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return {}, 204
        else:
            return {"status": "Not found"}, 400

    def perform_destroy(self, instance):
        db.session.delete(instance)
        db.session.commit()


class RetrieveMixin:
    """
    Retrieve a model instance.
    """

    def retrieve(self):
        instance = self.get_queryset()
        if instance:
            return self.schema.dump(instance), 200
        else:
            return {"status": "Not Found"}, 404


class ListMixin:
    """
    List a queryset.
    """

    def list(self):
        queryset = self.get_queryset()
        return self.schema.dump(queryset), 200


class GenericAPIView(
        CreateMixin,
        UpdateMixin,
        DestroyMixin,
        RetrieveMixin,
        ListMixin):
    model = None
    queryset = None
    schema = None

    def get_queryset(self):
        return self.queryset
