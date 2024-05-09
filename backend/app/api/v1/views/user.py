from app.api import api_v1_bp as bp
from flask import jsonify, request
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required
from app.api.errors import not_found
from app.models import User
from app import db


@bp.route("ping")
@jwt_required(optional=True)
def ping():
    return jsonify({"message": "Pong"}), 200


@bp.route("user/")
@jwt_required()
def get_user():
    user = current_user.to_dict()
    return jsonify(user), 200


@bp.route("user/<string:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return not_found("User does not exist")
    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "successfully deleted"})


@bp.route("user/<string:user_id>/", methods=["PUT"])
@jwt_required()
def user_update(user_id):
    user = User.query.filter_by(id=user_id).one_or_none()

    if not user:
        return not_found("User does not exist")
    user.update_user(**request.json)
    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict())
