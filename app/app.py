# -*- coding: utf-8 -*-
from datetime import date
from flask import Flask as _Flask
    # as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from app.libs.errors import Error
from app.models.bases import db


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise Error()


class Flask(_Flask):
    json_encoder = JSONEncoder
    pass


def register_blueprints(app):
    from app.api.v1.test.test import test
    from app.api.v1.user.user import user
    from app.api.v1.books.comment import book
    from app.api.v1.books.book import book as book_book
    from app.api.v1.token.token import token
    from app.api.v1.mails.mail import mail
    app.register_blueprint(test)
    app.register_blueprint(user)
    app.register_blueprint(book)
    app.register_blueprint(token)
    app.register_blueprint(mail)

    # api = Api(app)
    # api.add_resource(TodoList, '/todos')
    # api.add_resource(Todo, '/todos/<todo_id>')


def register_plugins(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    # app.config['JSON_AS_ASCII'] = False

    # 蓝图注册
    register_blueprints(app)
    # 注册SQLalchemy
    register_plugins(app)
    return app