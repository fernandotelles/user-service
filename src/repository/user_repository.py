from config import db
from src.models.user import User

class UserRepository:
    def all(self):
        return User.query.all()

    def get_by_id(self, id):
        user = User.query.filter_by(id = id).first()
        return user
    
    def delete(self, id):
        user = self.get_by_id(id)
        db.session.delete(user)
        db.session.commit()
       