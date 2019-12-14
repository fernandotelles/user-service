from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class UserService(Resource):
    def get(self):
        return {'hello': 'worldy'}

api.add_resource(UserService, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')