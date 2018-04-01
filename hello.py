#encoding: utf-8

from flask import Flask, request, jsonify, Response
import config
from models import Role, User
from exts import db
import json

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

#with app.app_context():
#    db.create_all()

@app.route('/')
def index():
    return 'isdndfdsex'

@app.route('/signup/', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return u'这是注册页面，请输入用户名和密码'
    else:
        username = request.get_json().get('username')
        password = request.get_json().get('password')
        telephone = request.get_json().get('telephone')
        if not User.query.filter_by(username=username).first():
            user = User(username=username, password=password, telephone=telephone)
            db.session.add(user)
            db.session.commit()
            return jsonify({
                "uid":user.id
            })
        else:
            return jsonify({
                "message":"Has already been signup"
            }),400

@app.route('/signin/', methods=['GET', 'POST'])
def singin():
    if request.method == 'GET':
        return u'这是登录页面，请输入账号密码'
    else:
        username = request.get_json().get('username')
        password = request.get_json().get('password')
        try:
            user = User.query.filter_by(username = username).first()
        except:
            user = None
        if user is not None and user.verify_password(password):
            return jsonify({
                "message":"success to signin"
            }), 200
        else:
            return jsonify({
                "message":"fail to signin"
            }), 401

if __name__ == '__main__':
    app.run()