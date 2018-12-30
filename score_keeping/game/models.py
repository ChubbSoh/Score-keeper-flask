from flask import Flask
from sqlalchemy import event, Table, Column, Integer, ForeignKey, UniqueConstraint, Index
from sqlalchemy.dialects import postgresql
from score_keeping import db, app
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.hybrid import hybrid_property
from score_keeping.helpers.utils import validation_preparation




class Game(db.Model):

    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    gameName = db.Column(db.String(20), unique=True, nullable=False)
    scorePerPoint = db.Column(db.Integer(), nullable=False)
    timerChecked = db.Column(db.Boolean, default=False)
    timerMinPerRound = db.Column(db.Integer())
    timerMinPerGame = db.Column(db.Integer())
    
  

    def __init__(self, user_id, gameName, scorePerPoint, timerChecked, timerMinPerRound, timerMinPerGame):
        self.gameName = gameName
        self.user_id = user_id
        self.scorePerPoint = scorePerPoint
        self.timerChecked = timerChecked
        self.timerMinPerRound = timerMinPerRound
        self.timerMinPerGame = timerMinPerGame


class GameLog(db.Model):

    __tablename__= 'gamelogs'

    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    scores = db.Column(MutableDict.as_mutable(postgresql.HSTORE))
     


    def __init__(self, game_id, scores):
        self.game_id = game_id
        self.scores = scores

        