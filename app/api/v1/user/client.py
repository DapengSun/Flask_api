# -*- coding: utf-8 -*-
from flask import Blueprint, request
from app.libs.errors_json import Success,Error
from app.libs.enums import ClientTypeEnums
from app.model_view.user import UserViewModel
from app.models.bases import db,submit
from app.models.users import Users
from app.validators.forms import ClientForms, ClientEmailForms, ClientPhoneForms
from . import client


@client.route('/v1/register',methods=['POST'])
def create_client():
    '''
    创建账户
    :return:
    '''
    try:
        data = request.json
        # 表单验证数据
        form = ClientForms(data).validate_for_api()

        # 字典实现方法对应
        types = {
            ClientTypeEnums.USER_EMAIL.value: create_client_by_email,
            ClientTypeEnums.USER_MOBILE.value: create_client_by_phone
        }
        types[form.type.value]()
        return Success(msg='创建账户成功')
    except Exception as ex:
        return Error(msg=f'创建账户异常',data=ex)



def create_client_by_email():
    '''
    通过Email创建账户
    :return:
    '''
    data = request.json
    emailForm = ClientEmailForms(data=data).validate_for_api()

    user = Users(account=emailForm.account.data,
                 nickname=emailForm.account.data,
                 email=emailForm.account.data,
                 password=emailForm.secret.data)
    # submit(user)
    return create_client_by_model(user)


def create_client_by_phone():
    '''
    通过Phone创建账户
    :return:
    '''
    data = request.json
    phoneForm = ClientPhoneForms(data=data).validate_for_api()

    user = Users(account=phoneForm.account.data,
                 nickname=phoneForm.account.data,
                 phone=phoneForm.account.data,
                 password=phoneForm.secret.data)
    # submit(user)
    return create_client_by_model(user)


def create_client_by_model(user):
    '''
    通过User模型创建账户
    :param user:
    :return:
    '''
    userViewModel = UserViewModel(user)
    flag = userViewModel.create_user()
    return True if flag == True else False


