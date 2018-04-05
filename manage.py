#encoding: utf-8


import sys
import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from app import db, app
from app.models import User, Article, Role, Permission, Comment

manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(
        app = app,
        db = db,
        User = User,
        Role = Role,
        Article = Article,
        Permission=Permission,
        Comment=Comment
    )

#manager.add_command('dbcreate', DBManger)
manager.add_command('shell', Shell(make_context=make_shell_context()))
manager.add_command('db', MigrateCommand)

@manager.command
def createdb():
    db.create_all()


if __name__ == '__main__':
    manager.run()