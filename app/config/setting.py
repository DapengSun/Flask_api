# -*- coding: utf-8 -*-

#设置连接数据库的URL
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:sdmp@127.0.0.1:3306/flask-api?charset=utf8'

# 设置每次请求结束后会自动提交数据库中的改动
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 查询时会显示原始SQL语句
SQLALCHEMY_ECHO = True

# JSON_AS_ASCII = False

# 分页参数设定
# 页面显示数量
PAGE_NUM = 10
# 起始页号
PAGE_INDEX = 1


SECRET_KEY = 'key'