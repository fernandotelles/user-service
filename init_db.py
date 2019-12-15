from config import db
from src.models.user import User

if __name__ == '__main__':
    db.create_all()
    db.session.add(User(name="John"))
    db.session.add(User(name="Lony"))
    db.session.commit()