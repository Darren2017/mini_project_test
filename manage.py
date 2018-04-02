#encoding: utf-8

import os
import sys
from flask_script import Manager, Shell
#from hello import app
#from db import DBManger
from flask_migrate import Migrate, MigrateCommand
from app import db, app
from app.models import User, Role

manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(
        app = app,
        db = db,
        User = User,
        Role = Role
    )

#manager.add_command('dbcreate', DBManger)
manager.add_command('shell', Shell(make_context=make_shell_context()))
manager.add_command('db', MigrateCommand)

@manager.command
def createdb():
    db.create_all()


if __name__ == '__main__':
    manager.run()