from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Genre).get(bid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, genre_data):
        data = Genre(**genre_data)
        self.session.add(data)
        self.session.commit()
        return data

    def delete(self, gid):
        genre = self.get_one(gid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, genre_data):  # WTF? All is done))
        genre = self.get_one(genre_data.get("id"))
        genre.name = genre_data.get("name")

        self.session.add(genre)
        self.session.commit()
