from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from helpers.decorators import admin_required, auth_required
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        req_json = request.json
        genre = director_service.create(req_json)
        return '', 201, {'location': f'/genres/{genre.id}'}


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @auth_required
    def get(self, did):
        data = director_service.get_one(did)
        final_data = DirectorSchema().dump(data)
        return final_data, 200

    @admin_required
    def put(self, did):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = did
        director_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, did):
        director_service.delete(did)
        return "", 204
