from flask import request
from flask_restx import Resource, Namespace
from implemented import user_service
from dao.model.user import UserSchema

users_ns = Namespace('users')


@users_ns.route('/')
class UsersView(Resource):
    def post(self):
        user_service.create(request.json)
        return '', 201

    def get(self):
        data = user_service.get_all()
        final_data = UserSchema(many=True).dump(data)
        return final_data, 200


@users_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        data = user_service.get_by_id(uid)
        final_data = UserSchema().dump(data)
        return final_data, 200

    def put(self, uid):
        req_json = request.json
        if 'id' not in req_json: # Зачем эта конструкция? Ведь по умолчанию идет обращение по ID?
            req_json['id'] = uid
        user_service.update(req_json)
        return '', 204

    def delete(self, uid):
        user_service.delete(uid)
        return '', 204



