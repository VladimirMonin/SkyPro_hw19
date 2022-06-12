from dao.model.user import User
from setup_db import db  # Надо ли?


class UserDAO:
    def __init__(self, User):
        self.User = User

    def get_one(self, uid):
        pass

    def get_by_user_name(self, username):
        pass

    def get_all(self):
        pass

    def create(self, user_data):
        pass

    def delete(self, uid):
        pass

    def update(self, user_data):
        pass
