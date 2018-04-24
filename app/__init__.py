# imports to be used in the application
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint

# initializing Blueprints
auth = Blueprint('auth', __name__)

# defining bootstrap
bootstrap = Bootstrap()
# creating the application
def create_app(config_state):
    # initializing the application
    app = Flask(__name__)
    app.config.from_object(config_options[config_state])

    # bootstrap initialization
    bootstrap.init_app(app)

    # registering main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
