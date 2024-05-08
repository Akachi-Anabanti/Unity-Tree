from app.api import api_v1_bp as bp
from flask import jsonify
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required


@bp.route("ping")
@jwt_required(optional=True)
def ping():
    return jsonify({"message": "Pong"}), 200


@bp.route("/user/")
@jwt_required()
def get_user():
    user = current_user.to_dict()
    return jsonify(user), 200
