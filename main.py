from flask import Flask
from flask_restx import Api

from config import Config
from dao.model.user import User
from setup_db import db
from views.auth import auth_ns
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.users import users_ns


def create_data(app, db):
    with app.app_context():
        db.create_all()

        u1 = User(username="vasya", password="my_little_pony", role="user")
        u2 = User(username="oleg", password="qwerty", role="user")
        u3 = User(username="vladimir", password="P@ssw0rd", role="admin")

        # pass_1 = 'my_little_pony'
        # pass_2 = 'qwerty'
        # pass_3 = 'P@ssw0rd'
        #
        # pass_1_hash = b'VZcOVtF7FILG5JoZQOGs6zgmJ/gPJOyEsaD8jBWJAVsgWKmZ0shk73WdxtrBP09eov/aIjlh+ItxMBBAlJbcwQ=='
        # pass_2_hash = b'lNKeNUqsW/oquYGLK5tDNPIcKUm12LRSRg7fN0MK59SWYQwd/wkPgjFF3HWzmaHLYK5Ykdm5ss+kduFVFtEcLQ=='
        # pass_3_hash = b'uUWTihX6z3lQzOufK6p8VDcJMprPQDmGMpyYzqTkvmzUrYlgLrGexzsK4r4AJl0OQj8IBx66YMrUXjrh2iiWpA=='

        with db.session.begin():
            db.session.add_all([u1, u2, u3])


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(users_ns)
    api.add_namespace(auth_ns)
    # TODO Спросить почему добавление происходит дважды за раз?
    # create_data(app, db)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run()
