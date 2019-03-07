# -*- coding: utf-8 -*-
from app.models.bases import db
from sqlalchemy import Column, Integer, String, SmallInteger, create_engine
from werkzeug.security import generate_password_hash


class Users(db.Model):
    __tablename__ = 'Users'

    id = Column(Integer,primary_key=True,autoincrement=True)
    account = Column(String(24),unique=True)
    nickname = Column(String(24),unique=True)
    auth = Column(SmallInteger,default=1)
    # password = Column('password',String(100))

    # @property
    # def password(self):
    #     return self.password
    #
    # @password.setter
    # def password(self,value):
    #     self.password = generate_password_hash('123456')

    def add_user(self):
        pass


