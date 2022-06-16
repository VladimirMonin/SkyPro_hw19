from flask import request
from flask_restx import Resource, Namespace
from implemented import auth_service  # TODO create object! Where?!
import logging

logging.basicConfig(encoding='utf-8', level=logging.INFO)  # Тут логирование на рботает. Только в сервисе

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        data = request.json
        logging.info(f'Данные полученные через POST запрос {data}')  # Тут логирование на рботает. Только в сервисе
        username = data.get('username', None)
        password = data.get('password', None)

        if None in [username, password]:
            return '', 401

        tokens = auth_service.generate_tokens(username, password)
        return tokens, 201

    def put(self):
        data = request.json
        refresh_token = data.get('refresh_token')

        tokens = auth_service.approve_refresh_token(refresh_token)
        return tokens, 201
