import jwt
from flask import request, abort
from config import Config


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer')[-1]

        try:
            jwt.decode(token, Config.JWT_SECRET, Config.JWT_ALGORITHM)
        except Exception as e:
            print('JWT decode ИСКЛЮЧЕНИЕ', e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer')[-1]
        role = None

        try:
            user = jwt.decode(token, Config.JWT_SECRET, Config.JWT_ALGORITHM)
            role = user.get('role', 'user')
        except Exception as e:
            print('JWT decode ИСКЛЮЧЕНИЕ', e)

        if role != 'admin':
            abort(403)

        return func(*args, **kwargs)

    return wrapper
