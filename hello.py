#encoding: utf-8
'''
from flask import Flask, request, jsonify, Response
import config
from models import Role, User
from exts import db
import json
from

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return 'isdndfdsex'


if __name__ == '__main__':
    app.run()'''

from manage import app

if __name__ == "__main__":
    app.run(host="localhost", port=5000)