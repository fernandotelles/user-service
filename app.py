from config import app, db
from flask_restful import Api
from src.services.user_service import UserService

api = Api(app)

api.add_resource(UserService, '/v1/users/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')