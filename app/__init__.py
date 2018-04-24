
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

t
h()

def create_app(config_state):
    app = Flask(__name__)
    app.config.from_object(config_options[config_state])


    bootstrap.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)		
    
    return app
from flask import Blueprint
auth = Blueprint('auth', __name__)

from . import views

