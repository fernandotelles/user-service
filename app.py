from config import app, db
from flask_restful import Api
from src.services.user_service import UserService, UserList

api = Api(app)

api.add_resource(UserList, '/v1/users/')
api.add_resource(UserService, '/v1/users/<user_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')