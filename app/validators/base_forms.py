# -*- coding: utf-8 -*-
from wtforms import Form

from app.libs.errors import FromsParameterException


class BaseForm(Form):
    '''
    重写Form的验证方法
    '''
    def __init__(self,data):
        super().__init__(data=data)


    def validate_for_api(self):
        valid = super().validate()
        if not valid:
            raise FromsParameterException(msg = self.errors)
        return self