#!/usr/bin/python3
from datetime import timedelta
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

"""Application configuration class"""


class Settings:

    JWT_COOKIE_SECURE = False
    JWT_COOKIE_SAMESITE = "Lax"
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "myn@tso0Very5ecre7key")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    REDIS_URL = "redis://localhost"

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
