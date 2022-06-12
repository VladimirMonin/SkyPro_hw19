from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        data = genre_service.get_all()
        final_data = GenreSchema(many=True).dump(data)
        return final_data, 200

    def post(self):
        req_json = request.json
        genre = genre_service.create(req_json)
        return '', 201, {'location': f'/genres/{genre.id}'}


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        data = genre_service.get_one(gid)
        final_data = GenreSchema().dump(data)
        return final_data, 200

    def put(self, gid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = gid
        genre_service.update(req_json)
        return "", 204

    def delete(self, gid):
        genre_service.delete(gid)
        return "", 204
