from app import db, bcrypt

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Network(db.Model):

    __tablename__ = "networks"

    id = db.Column(db.Integer, primary_key=True)
    net_name = db.Column(db.String, nullable=False, unique=True)
    owner_id = db.Column(db.Integer, ForeignKey('users.id'))

    def __init__(self, net_name):
        self.net_name = net_name

    def __repr__(self):
        return '<net_name {}'.format(self.net_name)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    networks = relationship("Network")

    def __init__(self, username, password, email):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<name {}'.format(self.username)