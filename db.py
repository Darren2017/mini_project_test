#encoding: utf-8

from flask_script import Manager
#from hello import app
from app import app


DBManger = Manager(app)

@DBManger.command
def createdb():
    db.create_all()
