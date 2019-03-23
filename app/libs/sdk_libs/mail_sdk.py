# -*- coding: utf-8 -*-
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL


class MailSdk(object):
    def __init__(self,model):
        self.mailModel = model
        pass

    def send_txt_mail(self):
        '''
        发送纯文本邮件
        :return:
        '''
        # ssl登录
        smtp = SMTP_SSL(self.mailModel.HostServer)
        # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        # smtp.set_debuglevel(1)
        smtp.ehlo(self.mailModel.HostServer)
        smtp.login(self.mailModel.SenderQQ, self.mailModel.Pwd)
        msg = MIMEText(self.mailModel.MailContent, "plain", 'utf-8')
        msg["Subject"] = Header(self.mailModel.MailTitle, 'utf-8')
        msg["From"] = self.mailModel.SenderQQMail
        msg["To"] = self.mailModel.Receiver
        smtp.sendmail(self.mailModel.SenderQQMail, self.mailModel.receiver_to_list, msg.as_string())
        smtp.quit()
        pass

    def send_html_mail(self):
        '''
        发送HTML邮件
        :return:
        '''
        # ssl登录
        smtp = SMTP_SSL(self.mailModel.HostServer)
        # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        # smtp.set_debuglevel(1)
        smtp.ehlo(self.mailModel.HostServer)
        smtp.login(self.mailModel.SenderQQ, self.mailModel.Pwd)
        msg = MIMEText(self.mailModel.MailContent, "html", 'utf-8')
        msg["Subject"] = Header(self.mailModel.MailTitle, 'utf-8')
        msg["From"] = self.mailModel.SenderQQMail
        msg["To"] = self.mailModel.Receiver
        smtp.sendmail(self.mailModel.SenderQQMail, self.mailModel.receiver_to_list, msg.as_string())
        smtp.quit()
        pass

    def send_html_with_img_mail(self):
        '''
        发送带图片的邮件
        :return:
        '''
        # ssl登录
        smtp = SMTP_SSL(self.mailModel.HostServer)
        # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        # smtp.set_debuglevel(1)
        smtp.ehlo(self.mailModel.HostServer)
        smtp.login(self.mailModel.SenderQQ, self.mailModel.Pwd)
        msg = MIMEMultipart('related')
        msg["Subject"] = Header(self.mailModel.MailTitle, 'utf-8')
        msg["From"] = self.mailModel.SenderQQMail
        msg["To"] = self.mailModel.Receiver

        msg = MIMEMultipart('related')
        content = MIMEText('<html><body><img src="cid:imageid" alt="imageid"></body></html>', 'html', 'utf-8')
        msg.attach(content)

        # 指定图片为当前目录
        fp = open('/Users/wangyiran/Desktop/12122227_123051482000_2.jpg', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        # 定义图片 ID，在 HTML 文本中引用
        msgImage.add_header('Content-ID', 'imageid')
        msg.attach(msgImage)

        smtp.sendmail(self.mailModel.SenderQQMail, self.mailModel.receiver_to_list, msg.as_string())
        smtp.quit()
        pass