# -*- coding: utf-8 -*-

from flask import Blueprint, request, json
from sqlalchemy import or_

from app.libs.errors_json import Success,Error
from app.libs.enums import ClientTypeEnums
from app.model_view.user import UserViewModel
from app.models.bases import db,commit
from app.models.users import Users
from app.validators.forms import ClientForms, ClientEmailForms, ClientPhoneForms
from . import user


@user.route('/v1/user',methods=['POST'])
def create_user():
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
            ClientTypeEnums.USER_EMAIL.value: create_user_by_email,
            ClientTypeEnums.USER_MOBILE.value: create_user_by_phone
        }
        types[form.type.value]()
        return Success(msg='创建账户成功')
    except Exception as ex:
        return Error(msg=f'创建账户异常',data=ex)


@user.route('/v1/user/<int:userId>',methods=['GET'])
def get_user(userId):
    '''
    获取指定用户
    :return:
    '''
    try:
        res = Users.query.filter(or_(Users.nickname == '13520387253',Users.email == 'dapeng@qq.com')).all()

        res_json = []
        for item in res:
            res_json.append(Users.to_json(item))
            pass

        return Success(msg='获取账号信息成功',data=res_json)
    except Exception as ex:
        return Error(msg=f'获取账号信息异常', data=ex)


@user.route('/v1/user/<int:userId>',methods=['DELETE'])
def del_user(userId):
    try:
        updateDict = {
            'sysStatus' : 1
        }
        res = Users.update_user(updateDict,id=userId)
        return Success(msg='删除账号信息成功')
    except Exception as ex:
        return Error(msg=f'删除账号信息异常',data=ex)
    pass


@user.route('/v1/user/<int:userId>',methods=['PUT'])
def put_user(userId):
    try:

        data = request.json
        # 表单验证数据
        form = ClientForms(data).validate_for_api()
        res = Users.update_user(form.data,id=userId)
        return Success(msg='更新账号信息成功')
    except Exception as ex:
        return Error(msg=f'更新账号信息异常',data=ex)
    pass

def create_user_by_email():
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
    return create_user_by_model(user)


def create_user_by_phone():
    '''
    通过Phone创建账户
    :return:
    '''
    data = request.json
    phoneForm = ClientPhoneForms(data=data).validate_for_api()

    # user = Users(account=phoneForm.account.data,
    #              nickname=phoneForm.account.data,
    #              phone=phoneForm.account.data,
    #              password=phoneForm.secret.data)
    user = Users()
    # user.password = phoneForm.secret.data
    user.nickname = phoneForm.account.data
    user.set_data(phoneForm.data)

    # submit(user)
    return create_user_by_model(user)


def create_user_by_model(user):
    '''
    通过User模型创建账户
    :param user:
    :return:
    '''
    userViewModel = UserViewModel(user)
    flag = userViewModel.create_user()
    return True if flag == True else False


