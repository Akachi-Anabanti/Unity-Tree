from api import api_v1_bp as bp
from flask import jsonify


@bp.route("ping")
def ping():
    return jsonify({}), 200
