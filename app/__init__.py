#coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import config



app = Flask(__name__)

#config_name = 'default'
app.config.from_object(config)
#config[config_name].init_app(app)


db = SQLAlchemy(app)

#初始化flask-login
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'



from .api import api
app.register_blueprint(api, url_prefix='/api')