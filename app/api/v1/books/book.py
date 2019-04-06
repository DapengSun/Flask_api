# coding:utf-8
import json

from flask import request, jsonify
from app.models.bases import commit
from app.models.book import Book
from . import book


@book.route('/v1/book/list/<int:user_id>',methods=['Get'])
def get_book(user_id):
    '''
    根据用户 获取图书
    :return:
    '''
    book = Book.query.filter_by(author=2).first()
    if not book:
        return jsonify(code=400,message='未找到指定图书')
    else:
        return jsonify(book)
    pass


@book.route('/v1/book/add',methods=['Post'])
def create_book():
    '''
    创建图书
    :return:
    '''
    data = request.json

    book = Book()
    book.set_data(data)
    commit(book)

    return jsonify(code=200,message='接口成功')
