from flask import Flask, jsonify
from flask_restx import Api, Resource, fields, Namespace

portal_namespace = Namespace('management', description= 'name space for the management')


@portal_namespace.route('/')
class HelloAuth(Resource):
    def get(self):
        return {"message": "Hello Auth nice to meet you"}

