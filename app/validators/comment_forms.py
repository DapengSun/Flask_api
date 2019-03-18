# -*- coding: utf-8 -*-
from wtforms import Form, StringField
from wtforms.validators import DataRequired, length
from app.validators.base_forms import BaseForm


class CommentForms(BaseForm):
    # def __init__(self,data):
    #     super().__init__(data=data)

    '''
    图书评论表单验证
    '''
    DoubanFilmId = StringField(validators=[DataRequired(message='图书ID不能为空')])
    ReviewTitle = StringField(validators=[DataRequired(message='评论标题不能为空'),
                                          length(min=5,max=20,message='评论标题不少于5个字，不超过20个字')])
    ReviewAuthorName = StringField(validators=[DataRequired(message='作者名称不能为空')])
    ReviewContent = StringField(validators=[DataRequired(message='评论内容不能为空')])
    pass