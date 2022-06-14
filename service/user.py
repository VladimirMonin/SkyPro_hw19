import hashlib
from config import Config
from dao.user import UserDAO


class UserService:
    def __int__(self, config: Config, dao: UserDAO):
        self.config = Config
        self.dao = UserDAO

    def get_hash(self, password):
        return hashlib.pbkdf2_hmac(  # Make yammy hash
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            Config.PWD_HASH_SALT,
            Config.PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")  # Convert bytes to final hash

    def get_by_id(self, uid):
        return self.dao.get_by_id(uid)
