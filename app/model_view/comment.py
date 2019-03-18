# -*- coding: utf-8 -*-
from app.models.bases import commit


class CommentViewModel(object):
    def __init__(self,data):
        self.comment = data

    def add_book_comment(self):
        '''
        新增图书评论
        :return:
        '''
        return commit(self.comment)
        pass
    pass