from flask import Flask
from sqlalchemy import event, Table, Column, Integer, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import validates
from score_keeping import db, app
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.hybrid import hybrid_property
from score_keeping.helpers.utils import validation_preparation
from flask_login import UserMixin
# import jwt


class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(), index=True, nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_hash = password
    
    # games = db.relationship('Game',
    #                 backref='user',
    #                 lazy=True,
    #                 order_by="desc(Game.id)",
    #                 cascade="delete, delete-orphan")    

    @validates('password_hash')
    @validation_preparation
    def set_password(self, key, password):
            if not password:
                self.validation_errors.append('Password not provided')

            if len(password) < 8 or len(password) > 50:
                self.validation_errors.append(
                    'Password must be between 8 and 50 characters')

            return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

