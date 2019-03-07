# -*- coding: utf-8 -*-
from flask import Blueprint

# blueprint
from app.libs.errors import FromsParameterException

test = Blueprint('test',__name__)


@test.route('/v1/test',methods=['GET'])
def get_data():
    raise FromsParameterException()
    # return '345'


@test.route('/',methods=['POST'])
def create_data():
    return 'successfully'
