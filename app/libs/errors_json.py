# -*- coding: utf-8 -*-
from flask import json
from werkzeug.exceptions import HTTPException


class ResBase(HTTPException):
    def __init__(self,code=None,msg=None,error_code=None,data=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        if data:
            self.data = data

        super().__init__(msg,None)

    def get_body(self, environ=None):
        """Get the Json body."""
        body = dict(
            code = self.code,
            error_code = self.error_code,
            msg = self.description,
            data = self.data
        )
        resMsg = json.dumps(body,default=lambda obj:obj.__dict__)
        return resMsg

    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]


class Success(ResBase):
    '''
    请求成功 - 200
    '''
    code = 200
    msg = 'request is ok'
    data = ''
    error_code = 0

    def __init__(self,code=None,msg=None,error_code=None,data=None):
        super().__init__(code=code,msg=msg,error_code=error_code,data=data)


class Error(ResBase):
    '''
    请求异常 - 500
    '''
    code = 500
    msg = 'sorry, wo make a mistake!'
    data = ''
    error_code = 500

    def __init__(self,code=None,msg=None,error_code=None,data=None):
        super().__init__(code=code,msg=msg,error_code=error_code,data=data)
