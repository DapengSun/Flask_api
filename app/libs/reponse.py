# -*- coding: utf-8 -*-
from flask import make_response, jsonify, request


def customer_response(*args,**kwargs):
    def inner(f):
        try:
            f(*args,**kwargs)
        except Exception as ex:
            return ex
    return inner