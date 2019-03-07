# -*- coding: utf-8 -*-
from wtforms import StringField, IntegerField

from app.validators.base_forms import BaseForm as Form
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError
from app.libs.enums import ClientTypeEnums


class ClientForms(Form):
    account = StringField(validators=[DataRequired(),length(min=5,max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self,value):
        client = ClientTypeEnums(value.data)
        self.type = client


class ClientEmailForms(ClientForms):
    '''
    继承ClientForms表单属性
    '''
    account = StringField(validators=[DataRequired(),Email(message='invalidate email')])
    secret = StringField(validators=[DataRequired(),Regexp(r'^[A-Z0-9a-z_*#@&$]{6,22}$')])
    nickname = StringField(validators=[DataRequired(),length(min=2,max=22)])

    def validate_account(self,value):
        pass