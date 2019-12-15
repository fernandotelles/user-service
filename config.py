from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/user.db'
app.config['SECRET_KEY'] = 'afacdd3132289db23325aaa6'
db = SQLAlchemy(app)