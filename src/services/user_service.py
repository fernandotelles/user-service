from flask_restful import Resource, fields, marshal_with
from src.repository.user_repository import UserRepository

resource_fields = {
    'id': fields.String,
    'name': fields.String
}

class UserService(Resource):

    repository = UserRepository()

    @marshal_with(resource_fields)
    def get(self):
        users = self.repository.all()
        return users, 200