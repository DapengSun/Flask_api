# -*- coding: utf-8 -*-
from wtforms import ValidationError

from app.models.bases import db, ModelBase
from sqlalchemy import Column, Integer, String, SmallInteger, create_engine, DateTime
from werkzeug.security import generate_password_hash
from datetime import datetime

# 通过flask-sqlacodegen实现数据库表映射model
# flask-sqlacodegen --outfile models.py --flask mysql+pymysql://root:sdmp@127.0.0.1:3306/flask-api


class Users(ModelBase):
    __tablename__ = 'Users'

    id = Column(Integer,primary_key=True,autoincrement=True)
    account = Column(String(24),unique=True)
    nickname = Column(String(24),unique=True)
    auth = Column(SmallInteger,default=1)
    _password = Column('password',String(100))
    phone = Column('phone',String(20))
    email = Column('email',String(50))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,value):
        self._password = generate_password_hash(value)

    def __repr__(self):
        return '<User {}>'.format(self.account)

    def add_user(self):
        pass

    @classmethod
    def get_user(cls,**kwargs):
        kwargs['SysStatus'] = 0
        return Users.query.filter_by(**kwargs)


    @classmethod
    def update_user(cls,updateDict,**kwargs):
        return Users.query.filter_by(**kwargs).update(updateDict)
        pass

    @classmethod
    def to_json(cls,obj):
        res_json = {
            'id' : obj.id,
            'account' : obj.account or '',
            'nickname': obj.nickname or '',
            'auth': obj.auth or '',
            'password': obj.password or '',
            'phone': obj.phone or '',
            'email': obj.email or '',
            'SysStatus': obj.SysStatus or '',
            'CreateTime': obj.CreateTime or ''
        }
        return res_json
        pass


class Comment(ModelBase):
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

