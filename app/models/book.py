# coding:utf-8
from sqlalchemy import Integer, Column, Index, String, ForeignKey
from app.models.bases import ModelBase


class Book(ModelBase):
    __tablename__ = 'Book'

    id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String(30),nullable=False)
    author = Column(Integer,ForeignKey('Users.id'))

    def keys(self):
        return ['id', 'name']

    def __getitem__(self, item):
        return getattr(self, item)
