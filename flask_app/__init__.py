from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .models import db
from .routes import main
from .config import Config

migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///surveys.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


 
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        db.create_all()

    
    app.register_blueprint(main)
    
    return app