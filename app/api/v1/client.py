# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify
from app.libs.errors import Success
from app.libs.enums import ClientTypeEnums
from app.models.bases import db
from app.models.users import Users
from app.validators.forms import ClientForms, ClientEmailForms

client = Blueprint('client',__name__)


@client.route('/v1/register',methods=['POST'])
def create_client():
    data = request.json
    # 表单验证数据
    form = ClientForms(data).validate_for_api()

    # 字典实现方法对应
    types = {
        ClientTypeEnums.USER_EMAIL.value: create_client_by_email
    }
    types[form.type.value]()

    return Success(msg='创建账户成功')


def create_client_by_email():
    data = request.json
    emailForm = ClientEmailForms(data=data).validate_for_api()

    try:
        user = Users(account=emailForm.account.data,nickname=emailForm.nickname.data)
        user.password = emailForm.secret.data
        db.session.add(user)
        db.session.commit()
        db.session.close()
    except Exception as ex:
        print(ex)