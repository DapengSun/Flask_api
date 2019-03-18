# -*- coding: utf-8 -*-
from flask import request
from sqlalchemy import and_, or_

from app.libs.errors_json import Success, Error
from app.models.comment import Comment
from . import book


@book.route('/v1/book/comment/<string:keyword>',methods=['GET'])
def get_book_comment(keyword):
    '''
    查找图书评价
    :return:
    '''
    try:
        res = Comment.query.filter(or_(Comment.ReviewTitle.like(keyword + '%'),
                                        Comment.ReviewAuthorName.like(keyword + '%'))).all()
        resList = []
        for item in res:
            resList.append(Comment.to_json(item))
        return Success(msg='获取图书评论成功',data=resList)
        pass
    except Exception as ex:
        return Error(msg='获取图书评论异常',data=ex)
        pass
    pass


@book.route('/v1/book/commment',methods=['POST'])
def add_book_comment():

    try:
        pass
    except Exception as ex:
        return Error(msg='新增图书评论异常',data=ex)
        pass
    pass