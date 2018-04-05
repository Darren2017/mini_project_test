#coding:utf-8
from flask import jsonify, request, session
from . import api
from app import db, app
from app.models import User, Article
from decorators import login_required

@api.route('/article/<int:articleid>', methods=['GET', 'POST'])
@login_required
def readarticle(articleid):
    if request.method == 'GET':
        return u'this is article'
    else:
        title = request.get_json().get('title')
        content = request.get_json().get('content')
        article = Article(title=title, content=content)
        user_id = 1#session.get('user_id')
        user = User.query.filter_by(id=user_id).first()
        article.author = user
        db.session.add(article)
        db.session.commit()
        return jsonify({
                "title":article.title
            }), 200