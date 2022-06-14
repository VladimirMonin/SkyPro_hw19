import hashlib
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

    def get_hash(self, password): #TODO Стереть ЭТО. И сделать микро методы. base64 encode/decode hash отдельно всё раздробить В ХАШУ!
        return hashlib.pbkdf2_hmac(  # Make yammy hash
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            self.config.PWD_HASH_SALT,
            self.config.PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")  # Convert bytes to final hash

    def get_by_username(self, username):
        pass

    def compare_password(self, password_hash, password):

        pass
