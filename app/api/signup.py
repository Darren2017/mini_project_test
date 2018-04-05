#encoding: utf-8

from flask import jsonify, request
from app import db
from . import api
import json
from flask_login import login_user, logout_user, current_user, login_required
from ..models import User, Role, Article


@api.route("/signup/", methods=['GET', 'POST'])
def signup():
    if request.method == "GET":
        return u'这是注册页面，请输入用户名和密码'
    else:
        username = request.get_json().get('username')
        password = request.get_json().get('password')
        telephone = request.get_json().get('telephone')
        email = request.get_json().get('email')
        if not User.query.filter_by(username=username).first():
            user = User(username=username, password=password, telephone=telephone, email=email)
            db.session.add(user)
            db.session.commit()
            return jsonify({
                "uid":user.id
            }),200
        else:
            return jsonify({
                "message":"Has already been signup"
            }),400