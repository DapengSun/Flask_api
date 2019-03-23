# -*- coding: utf-8 -*-
from wtforms import StringField
from wtforms.validators import DataRequired
from app.validators.base_forms import BaseForm


class MailForms(BaseForm):
    SenderQQ = StringField(validators=[DataRequired(message='发件人的QQ号码不能为空')])
    SenderQQMail = StringField(validators=[DataRequired(message='发件人的邮箱不能为空')])
    Receiver = StringField(validators=[DataRequired(message='收件人邮箱不能为空')])
    MailContent = StringField(validators=[DataRequired(message='邮件的正文内容不能为空')])
    MailTitle = StringField(validators=[DataRequired(message='邮件标题不能为空')])

    # HostServer = HostServer
    # # sender_qq为发件人的qq号码
    # self.SenderQQ = SenderQQ
    # # pwd为qq邮箱的授权码
    # self.Pwd = Pwd
    # # 发件人的邮箱
    # self.SenderQQMail = SenderQQMail
    # # 收件人邮箱
    # self.Receiver = Receiver
    # # 邮件的正文内容
    # self.MailContent = MailContent
    # # 邮件标题
    # self.MailTitle = MailTitle
    pass