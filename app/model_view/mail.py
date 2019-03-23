# -*- coding: utf-8 -*-
from app.libs.sdk_libs.mail_sdk import MailSdk


class MailViewModel(object):
    def __init__(self,model):
        self.mailModel = model
        pass

    '''
    Mail模型Model层
    '''
    def send_txt_mail(self):
        mailSdk = MailSdk(self.mailModel)
        mailSdk.send_txt_mail()
        pass

    def send_html_mail(self):
        mailSdk = MailSdk(self.mailModel)
        mailSdk.send_html_mail()
        pass

    def send_html_with_img_mail(self):
        mailSdk = MailSdk(self.mailModel)
        mailSdk.send_html_with_img_mail()
        pass
