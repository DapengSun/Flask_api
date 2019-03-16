# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy, BaseQuery
from sqlalchemy import Column, DateTime, SmallInteger

db = SQLAlchemy()


def commit(model):
    '''
    提交Model
    :param model:
    :return:
    '''
    try:
        db.session.add(model)
        db.session.commit()
        db.session.close()
        return True
    except Exception as ex:
        db.session.rollback()
        raise ex


class ModelBase(db.Model):
    '''
    数据基类
    '''
    __abstract__ = True

    CreateTime = Column('CreateTime',DateTime)
    SysStatus = Column('SysStatus',SmallInteger,default=0)

    def set_data(self,data_dict):
        for key,value in data_dict.items():
            if hasattr(self,key):
                setattr(self,key,value)
                pass
            pass
        pass
    pass

