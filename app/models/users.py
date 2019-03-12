# -*- coding: utf-8 -*-
from app.models.bases import db
from sqlalchemy import Column, Integer, String, SmallInteger, create_engine
from werkzeug.security import generate_password_hash

# 通过flask-sqlacodegen实现数据库表映射model
# flask-sqlacodegen --outfile models.py --flask mysql+pymysql://root:sdmp@127.0.0.1:3306/flask-api


class Users(db.Model):
    __tablename__ = 'Users'

    id = Column(Integer,primary_key=True,autoincrement=True)
    account = Column(String(24),unique=True)
    nickname = Column(String(24),unique=True)
    auth = Column(SmallInteger,default=1)
    password = Column('password',String(100))
    phone = Column('phone',String(20))
    email = Column('email',String(50))

    def __repr__(self):
        return '<User {}>'.format(self.account)

    def add_user(self):
        pass

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

