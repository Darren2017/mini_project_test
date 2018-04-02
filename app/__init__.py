from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)

#config_name = 'default'
app.config.from_object(config)
#config[config_name].init_app(app)

#bootstrap.init_app(app)
#db.init_app(app)

#bootstrap = Bootstrap()
db = SQLAlchemy(app)

from .api import api
app.register_blueprint(api, url_prefix='/api')