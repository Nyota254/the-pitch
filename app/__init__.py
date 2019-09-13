from flask import Flask
from flask_bootstrap import Bootstrap
from config import configurations
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(configname):

    app.config.from_object(configurations[configname])

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    bootstrap.init_app(app)
    db.init_app(app)

    return app