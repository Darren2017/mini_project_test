#coding:utf-8
from flask import jsonify, request, session
from . import api
from app import db, app
from app.models import User, Article, Comment
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
        user_id = session.get('user_id')
        user = User.query.filter_by(id=user_id).first()
        article.author = user
        db.session.add(article)
        db.session.commit()
        return jsonify({
                "title":article.title
            }), 200

@api.route('/article/<int:articleid>/comment/', methods=['POST'])
@login_required
def add_comment(articleid):
    comment = request.get_json().get("comment")
    article_id = request.get_json().get("article_id")
    comment = Comment(comment=comment)
    user_id = session.get('user_id')
    user = User.query.filter_by(id=user_id).first()
    comment.author = user
    article = Article.query.filter_by(id=article_id).first()
    comment.article = article
    db.session.add(comment)
    db.session.commit()
    return jsonify({
                "result":"success to add comment"
            }), 200
