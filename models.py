# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, SmallInteger, String
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Comment(db.Model):
    __tablename__ = 'Comment'

    ID = db.Column(db.Integer, primary_key=True)
    DoubanFilmId = db.Column(db.String(50))
    ReviewTitle = db.Column(db.String(200))
    ReviewLink = db.Column(db.String(200))
    ReviewAuthorAvatar = db.Column(db.String(200))
    ReviewAuthorName = db.Column(db.String(200))
    ReviewScore = db.Column(db.String(50))
    ReviewDate = db.Column(db.DateTime)
    ReviewContent = db.Column(db.String)
    ReviewReturn = db.Column(db.Integer)
    CDate = db.Column(db.DateTime)
    ReviewScoreName = db.Column(db.String(50))
    DoubanFilmReviewId = db.Column(db.String(50))


class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    auth = db.Column(db.SmallInteger)
    account = db.Column(db.String(24), unique=True)
    nickname = db.Column(db.String(24), unique=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(100))
    phone = db.Column(db.String(20))
