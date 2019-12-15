from config import db
from src.models.user import User

class UserRepository:
    def all(self):
        return User.query.all()
