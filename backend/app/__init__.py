#!/usr/bin/python3

"""Initializes the whole application"""
from flask import Flask
from flask_jwt_extended import JWTManager
from app.config import Settings
from .db_engine import db
from flask_cors import CORS
from flask_migrate import Migrate

jwt = JWTManager()
migrate = Migrate()


def create_app(config_name=Settings):
    app = Flask(__name__)
    app.config.from_object(config_name)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from .api import api_v1_bp as api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api/v1")

    return app
