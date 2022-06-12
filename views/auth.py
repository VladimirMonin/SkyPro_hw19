from flask import request
from flask_restx import Resource, Namespace

auth_ns = Namespace('auth')
class AuthsView(Resource):
    def post(self):
        data = request.json

        username = data.get('username', None)
        password = data.get('password', None)

        if None in [username, password]:
            return '', 401

        tokens = auth.service.generate_tokens(username, password)
        return tokens, 201

    def put(self):
        data = request.json
        refresh_token = data.get('refresh_token')

        tokens = auth.service.approve_refresh_token(refresh_token)
        return tokens, 201