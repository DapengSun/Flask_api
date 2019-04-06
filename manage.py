# -*- coding: utf-8 -*-
from flask import current_app
from flask_script import Manager,Command
from flask_migrate import Migrate, MigrateCommand
from app.app import create_app
from app.model_view.mail import MailViewModel
from app.models import users
from app.models import department
from app.models.bases import db
from app.models.mail import Mail
from app.models.book import Book

app = create_app()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def test_send_mail():
    with app.app_context():
        mail = Mail(HostServer=current_app.config['MAIL_HOST_SERVER'],
                    Pwd = current_app.config['MAIL_AUTH_CODE'],
                    SenderQQ='1215404991',
                    SenderQQMail='1215404991@qq.com',
                    Receiver='13520387252@163.com',
                    MailContent='测试内容',
                    MailTitle='测试标题')

        mailView = MailViewModel(mail)
        mailView.send_txt_mail()
    pass

if __name__ == '__main__':
    manager.run()
    # test_send_mail()