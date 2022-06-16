import calendar
import datetime
import jwt

from flask_restx import abort
from service.user import UserService
from config import Config
import logging

logging.basicConfig(encoding='utf-8', level=logging.INFO)

class AuthService:
    def __init__(self, user_service: UserService, config: Config):  # TODO Узнать об этом двоеточии
        self.user_service = user_service
        self.config = config

    def generate_tokens(self, username, password, is_refresh=False):
        user = self.user_service.get_by_username(username)
        logging.info(f'Получен список объектов User: {user}')
        user = user[0]
        if user is None:
            logging.info(f'Не передан пароль или логин')
            raise abort(404)
        if not is_refresh:
            logging.info(f'Refresh токена нет. Будет происходить сверка пароля')
            if not self.user_service.compare_password(user.password, password):
                logging.info(f'Проверка пароля не пройдена. Пароли не совпадают')
                abort(400)

        logging.info(f'Проверка пароля пройдена. Начанием формировать токены')

        data = {
            'username': user.username,
            'role': user.role
        }

        # 30 minutes for access token
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, Config.JWT_SECRET, algorithm=Config.JWT_ALGORITHM)

        # 130 days for refresh_token
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, Config.JWT_SECRET, algorithm=Config.JWT_ALGORITHM)

        logging.info(f'Сформированы токены access_token: {access_token},'
                     f'refresh_token: {refresh_token}')

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(refresh_token, Config.JWT_SECRET, Config.JWT_ALGORITHM)
        username = data.get('username')

        return self.generate_tokens(username, None, is_refresh=True)


