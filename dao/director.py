from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, director_data):
        data = Director(**director_data)
        self.session.add(data)
        self.session.commit()
        return data

    def delete(self, did):
        director = self.get_one(did)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_data):
        director = self.get_one(director_data.get("id"))
        director.name = director_data.get("name")

        self.session.add(director)
        self.session.commit()
