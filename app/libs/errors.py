# -*- coding: utf-8 -*-
from flask import json, request
from werkzeug.exceptions import HTTPException


# 重写HTTPException异常中的get_body和get_headers方法,返回异常json格式
class APIException(HTTPException):
    code = 500
    msg = 'sorry, wo make a undefined mistake!'
    error_code = 999

    def __init__(self,msg=None,code=None,error_code=None,header=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super().__init__(msg,None)


    def get_body(self, environ=None):
        """
        Get the HTML body.
        重写父类的方法
        """
        body = dict(
            code = self.code,
            error_code = self.error_code,
            requert = request.method + " " + request.base_url,
            description = self.description
        )
        text = json.dumps(body)
        return text


    def get_headers(self, environ=None):
        """
        Get a list of headers.
        重写父类的方法
        """
        return [('Content-Type', 'application/json')]


class FromsParameterException(APIException):
    code = 500001
    description = (
        'WTForms Parameter Error!'
    )


class Success(APIException):
    code = 200
    msg = 'OK'
    error_code = 0

    def __init__(self, msg=None, code=None, error_code=None, header=None):
        super().__init__(msg=msg, code=code, error_code=error_code, header=header)


class Error(APIException):
    code = 500
    msg = 'Error'
    error_code = 500

    def __init__(self, msg=None, code=None, error_code=None, header=None):
        super().__init__(msg=msg, code=code, error_code=error_code, header=header)