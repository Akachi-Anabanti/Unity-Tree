#!/usr/bin/python3

"""Initializes the whole application"""
from flask import Flask
from flask_jwt_extended import JWTManager
from app.config import Settings
from .db_engine import db
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sse import sse
from .file_service import FileService

jwt = JWTManager()
migrate = Migrate()
file_service = FileService(Settings.UPLOAD_FOLDER, Settings.ALLOWED_EXTENSIONS)


def create_app(config_name=Settings):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(config_name)

    CORS(
        app,
        resources={r"/api/v1/*": {"origins": "*"}},
        supports_credentials=True,
    )

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from .api import api_v1_bp as api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api/v1")
    app.register_blueprint(sse, url_prefix="/stream")
    return app
