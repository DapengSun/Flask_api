# -*- coding: utf-8 -*-
from flask import jsonify, g
from app.models.users import Users
from . import token
from app.models.bases import auth


@token.route('/api/token',methods=['GET'])
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({ 'token': token.decode('ascii') })


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = Users.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = Users.query.filter_by(account = username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True