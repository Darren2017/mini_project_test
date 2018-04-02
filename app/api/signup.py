#encoding: utf-8

from flask import jsonify, request
from app import db
from . import api
from ..models import User, Role
import json

@api.route('/signup/', methods=['GET','POST'])
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
            }),200
        else:
            return jsonify({
                "message":"Has already been signup"
            }),400