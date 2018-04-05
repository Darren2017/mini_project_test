#encoding: utf-8
import os

DEBUG = True

SECRET_KEY = os.urandom(24)

DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'tam'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_first_j'

FLASKY_ADMIN = '17362990052@163.com'

SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,
    DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

SQLAdLCHEMY_TRACK_MODIFICATIONS = False