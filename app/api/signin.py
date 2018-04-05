#encoding: utf-8
from . import api
from flask import jsonify, request, session
from app import db
from app.models import User, Role, Article
import json


@api.route('/signin/', methods=['GET', 'POST'])
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
            session['user_id'] = user.id
            session.permanent = True
            return jsonify({
                "uid":user.id
            }), 200
        else:
            return jsonify({
                "message":"fail to signin"
            }), 400