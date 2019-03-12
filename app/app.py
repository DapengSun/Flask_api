# -*- coding: utf-8 -*-
from flask import Flask
from app.models.bases import db


def register_blueprints(app):
    from app.api.v1.test import test
    from app.api.v1.user.client import client
    app.register_blueprint(test)
    app.register_blueprint(client)


def register_plugins(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


def register_error_handler(app):
    pass


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')

    # 蓝图注册
    register_blueprints(app)
    # 注册SQLalchemy
    register_plugins(app)
    return app