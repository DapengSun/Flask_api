# -*- coding: utf-8 -*-
from flask import Flask
from flask_restplus import Api
from app.api.v1.test.test import TodoList, Todo
from app.models.bases import db


def register_blueprints(app):
    from app.api.v1.test.test import test
    from app.api.v1.user.user import user
    from app.api.v1.books.comment import book
    app.register_blueprint(test)
    app.register_blueprint(user)
    app.register_blueprint(book)

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