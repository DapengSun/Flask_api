# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.bases import ModelBase


class Department(ModelBase):
    __tablename__ = 'Department'

    ID = Column(Integer,primary_key=True)
    Name = Column(String(30))

    users = relationship('Users',backref='Department')
    pass