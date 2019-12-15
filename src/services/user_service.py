from flask_restful import Resource, fields, marshal_with, reqparse, abort
from src.repository.user_repository import UserRepository

resource_fields = {
    'id': fields.String,
    'name': fields.String
}

repository = UserRepository()

parser = reqparse.RequestParser()
parser.add_argument('user_id', location='json')
parser.add_argument('user_name', location='json')

def abort_if_dont_exists(user_id):
    user = repository.get_by_id(user_id)
    if user == None:
        abort(404, message="User {} doesn't exist".format(user_id))

def argsToDict(args):
    user = {}
    user['id'] = args['user_id']
    user['name'] = args['user_name']
    return user

class UserService(Resource):
    @marshal_with(resource_fields)
    def get(self, user_id):
        abort_if_dont_exists(user_id)
        return repository.get_by_id(user_id), 200
    
    def delete(self, user_id):
        abort_if_dont_exists(user_id)
        repository.delete(user_id)
        return '', 204
    
    def put(self, user_id):
        abort_if_dont_exists(user_id)
        args = parser.parse_args()
        user = argsToDict(args)
        repository.update(user)
        return '', 204

class UserList(Resource):
    @marshal_with(resource_fields)
    def get(self):
        users = repository.all()
        return users, 200
