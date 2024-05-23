from flask import Blueprint

api_v1_bp = Blueprint("api_v1", __name__)

from .v1.views.user import *
from .v1.views.family_member import *
from .v1.views.auth import *
from .v1.views.media import *
