import base64
import hashlib
import hmac

from config import Config
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO, config: Config):
        self.dao = dao
        self.config = config

    def get_by_id(self, uid):
        return self.dao.get_by_id(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, uid):
        return self.dao.create(uid)

    def update(self, req_json):
        self.dao.update(req_json)

    def delete(self, uid):
        self.dao.delete(uid)

    def get_pass_hash(self, password):
        """Основной метод для хеширования паролей
        return: str # для записи в БД
        """
        pass_hash = self.hash_it(password)
        b64_hash = self.encode_base64(pass_hash)
        return b64_hash

    def encode_base64(self, data):
        """Кодирует из 8-бит в нормальную строку
        для записи в БД и чтения человеками"""
        return base64.b64encode(data)

    def decode_base64(self, data):
        """Декодирует из нормального вида в 8-бит
        для чтения роботами"""
        return base64.b64decode(data)

    def hash_it(self, data):
        """Делает хеш и отдает байтовую строку 8-бит"""
        return hashlib.pbkdf2_hmac(self.config.HASH_ALGORITHM,
                                   data.encode('utf-8'),
                                   self.config.PWD_HASH_SALT,
                                   self.config.PWD_HASH_ITERATIONS)

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def compare_password(self, password_hash, password) -> bool:
        """Декодирует пароль из БД в 8бит строку
        Хеширует вводимый пароль и потом сравнивает их"""
        db_bass_decode = self.decode_base64(password_hash)
        try_password_hash = self.hash_it(password)
        return hmac.compare_digest(db_bass_decode, try_password_hash)
