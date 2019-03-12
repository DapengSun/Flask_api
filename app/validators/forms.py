# -*- coding: utf-8 -*-
from wtforms import StringField, IntegerField, validators
from app.validators.base_forms import BaseForm as Form
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError
from app.libs.enums import ClientTypeEnums


class ClientForms(Form):
    account = StringField(validators=[DataRequired(),length(min=5,max=32)])
    secret = StringField(validators=[DataRequired(),
                                     Regexp(r'^[A-Z0-9a-z_*#@&$]{6,22}$',
                                     message = '密码验证失败，清输入6-22位密码')])
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self,value):
        client = ClientTypeEnums(value.data)
        self.type = client


class ClientEmailForms(ClientForms):
    '''
    继承ClientForms表单属性
    '''
    account = StringField(validators=[DataRequired(),Email(message='invalidate email')])

    def validate_account(self,value):
        pass


class ClientPhoneForms(ClientForms):
    '''
    继承ClientForms表单属性
    '''
    account = StringField(validators=[DataRequired()])

    def validate_account(self,value):
        import re
        flag = re.match(r'1\d{10}',value.data)
        return flag