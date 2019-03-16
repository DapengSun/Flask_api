# -*- coding: utf-8 -*-
from app.models.bases import commit
from app.models.users import Users


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
        return commit(self.user)

    def get_user(self):
        '''
        查询用户
        :return:
        '''
        pass
