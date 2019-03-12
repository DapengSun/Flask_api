# -*- coding: utf-8 -*-
from app.models.bases import submit


class UserViewModel(object):
    '''
    User模型Model层
    '''
    def __init__(self,user):
        self.user = user

    def create_user(self):
        '''
        创建用户
        :return: true / false
        '''
        return submit(self.user)