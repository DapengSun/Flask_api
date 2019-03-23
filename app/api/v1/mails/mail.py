# -*- coding: utf-8 -*-
from flask import g, request, current_app
from app.libs.errors import Success
from app.model_view.mail import MailViewModel
from app.models.mail import Mail
from app.validators.mail_forms import MailForms
from . import mail
from app.models.bases import auth


@mail.route('/v1/mail',methods=['POST'])
@auth.login_required
def get_user_mail():
    '''
    获取用户邮件
    :return:
    '''
    # print(g.user)
    # 表单验证
    data = request.json
    mail_form_data = MailForms(data).validate_for_api()
    # 模型赋值
    mailModel = Mail()
    mailModel.set_data(mail_form_data.data)
    mailModel.HostServer = current_app.config['MAIL_HOST_SERVER']
    mailModel.Pwd = current_app.config['MAIL_AUTH_CODE']

    mailViewModel = MailViewModel(mailModel)
    # mailViewModel.send_txt_mail()
    mailViewModel.send_html_with_img_mail()

    return Success(msg='发送邮件成功')
    pass