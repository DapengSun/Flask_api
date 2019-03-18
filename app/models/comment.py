# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, DateTime

from app.models.bases import ModelBase


class Comment(ModelBase):
    __tablename__ = 'Comment'

    ID = Column(Integer, primary_key=True)
    DoubanFilmId = Column(String(50))
    ReviewTitle = Column(String(200))
    ReviewLink = Column(String(200))
    ReviewAuthorAvatar = Column(String(200))
    ReviewAuthorName = Column(String(200))
    ReviewScore = Column(String(50))
    ReviewDate = Column(DateTime)
    ReviewContent = Column(String)
    ReviewReturn = Column(Integer)
    CDate = Column(DateTime)
    ReviewScoreName = Column(String(50))
    DoubanFilmReviewId = Column(String(50))

    @classmethod
    def to_json(cls, obj):
        if obj:
            res_json = {
                'ID': obj.ID,
                'DoubanFilmId': obj.DoubanFilmId or '',
                'ReviewTitle': obj.ReviewTitle or '',
                'ReviewLink': obj.ReviewLink or '',
                'ReviewAuthorAvatar': obj.ReviewAuthorAvatar or '',
                'ReviewAuthorName': obj.ReviewAuthorName or '',
                'ReviewDate': str(obj.ReviewDate) or '',
                'ReviewContent': obj.ReviewContent or '',
                'ReviewReturn': obj.ReviewReturn or '',
                'CDate': str(obj.CDate) or '',
                'ReviewScoreName': obj.ReviewScoreName or '',
                'DoubanFilmReviewId': obj.DoubanFilmReviewId or ''
            }
            return res_json
        else:
            return ''
        pass