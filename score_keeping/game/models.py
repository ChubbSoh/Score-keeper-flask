from flask import Flask
from sqlalchemy import event, Table, Column, Integer, ForeignKey, UniqueConstraint, Index
from score_keeping import db, app
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.hybrid import hybrid_property
from score_keeping.helpers.utils import validation_preparation



class Game(db.Model):

    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    gameName = db.Column(db.String(20), unique=True, nullable=False)
    scorePerPoint = db.Column(db.Integer(), nullable=False)
    timerChecked = db.Column(db.Boolean, default=False)
    timerMinPerRound = db.Column(db.Integer())
    timerMinPerGame = db.Column(db.Integer())
    


  

    def __init__(self, gameName, scorePerPoint, timerChecked, timerMinPerRound, timerMinPerGame):
        self.gameName = gameName
        self.scorePerPoint = scorePerPoint
        self.timerChecked = timerChecked
        self.timerMinPerRound = timerMinPerRound
        self.timerMinPerGame = timerMinPerGame
