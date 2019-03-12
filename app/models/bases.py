# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def submit(model):
    try:
        db.session.add(model)
        db.session.commit()
        db.session.close()
        return True
    except Exception as ex:
        db.session.rollback()
        raise ex
