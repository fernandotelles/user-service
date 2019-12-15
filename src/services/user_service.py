from flask_restful import Resource, fields, marshal_with, reqparse, abort
from src.repository.user_repository import UserRepository

resource_fields = {
    'id': fields.String,
    'name': fields.String
}

repository = UserRepository()

def abort_if_dont_exists(user_id):
    user = repository.get_by_id(user_id)
    if user == None:
        abort(404, message="User {} doesn't exist".format(user_id))

class UserService(Resource):
    @marshal_with(resource_fields)
    def get(self, user_id):
        abort_if_dont_exists(user_id)
        return repository.get_by_id(user_id), 200

class UserList(Resource):
    @marshal_with(resource_fields)
    def get(self):
        users = repository.all()
        return users, 200
