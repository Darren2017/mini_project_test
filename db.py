#encoding: utf-8

from flask_script import Manager
from hello import app


DBManger = Manager(app)

@DBManger.command
def createdb():
    db.create_all()

@DBManger.command
def init():
    print '数据库初始化成功'

@DBManger.command
def migrate():
    print '数据表迁移成功'