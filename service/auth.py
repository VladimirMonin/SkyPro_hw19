import calendar
import datetime
import jwt

from flask_restx import abort
from service.user import UserService
from config import Config


class AuthService:
    def __int__(self, user_service: UserService, config: Config):  # TODO Узнать об этом двоеточии
        self.user_service = user_service
        self.config = config

    def generate_tokens(self, username, password):
        user = self.user_service.get_by_username(username)

        if user in None:
            raise abort(404)

        if not self.user_service.compare_password(user.password, password):
            abort(400)

        data = {
            'username': user.username,
            'role': user.role
        }

        # 30 minutes for access token
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, self.config.JWT_SECRET, algorithm=self.config.JWT_ALGORITHM)

        # 130 days for refresh_token
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, self.config.JWT_SECRET, algorithm=self.config.JWT_ALGORITHM)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def approve_refresh_token(self):
        pass
