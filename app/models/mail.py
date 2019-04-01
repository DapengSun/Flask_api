# -*- coding: utf-8 -*-
from sqlalchemy import String, Column

from app.model_view.mail import MailViewModel
from app.models.bases import ModelBase


class Mail(ModelBase):
    __abstract__ = True

    HostServer = Column(String(20))
    SenderQQ = Column(String(50))
    Pwd = Column(String(20))
    SenderQQMail = Column(String(200))
    Receiver = Column(String(50))
    MailContent = Column(String(200))
    MailTitle = Column(String(50))

    def __init__(self,**param_list):
        for param in param_list.keys():
            self.__setattr__(param,param_list[param])
            pass
        pass

    @property
    def receiver_to_list(self):
        '''
        Receiver逗号分割 转 list
        :return:
        '''
        receiverList = self.Receiver.split(',')
        return receiverList
        pass
    pass