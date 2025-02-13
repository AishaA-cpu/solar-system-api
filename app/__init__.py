from flask import Flask, config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
load_dotenv()

db = SQLAlchemy() # why is this outside the create app funtion
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if not test_config:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
        app.config['SQLALCHEMY_ECHO'] = True
    else:
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
        app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
    migrate.init_app(app, db)

    # import model
    from app.models.planets import Planet

    from .routes import planets_bp
    app.register_blueprint(planets_bp)

    return app
