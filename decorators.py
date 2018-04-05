#coding:utf-8
from functools import wraps
from flask import session, jsonify, redirect, url_for

#登录限制装饰器
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return jsonify({
                "message":"fail to signin"
            }), 401
    return wrapper