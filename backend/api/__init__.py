from flask import Blueprint

api_v1_bp = Blueprint("api_v1", __name__)

from api.v1.views.user import *
