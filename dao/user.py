from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_data):
        pass

    def delete(self, uid):
        user = self.get_by_id(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, req_json):
        user = self.get_by_id(req_json.get("id"))
        user.username = req_json.get('username')
        user.password = req_json.get('password')
        user.role = req_json.get('role')

        self.session.add(user)
        self.session.commit()
