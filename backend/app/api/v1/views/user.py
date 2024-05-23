from flask_jwt_extended import current_user, jwt_required
from app.api import api_v1_bp as bp
from flask import jsonify, request
from app.api.errors import not_found, bad_request
from app.api.v1.controllers import user_controller as ctrl
from app.models import User, Member


@bp.route("ping")
@jwt_required(optional=True)
def ping():
    return jsonify({"msg": "Pong"}), 200


@bp.route("user/")
@jwt_required()
def get_user():
    user_info = ctrl.get_user_info(current_user)
    return jsonify(user_info), 200


@bp.route("user/family-created/")
@jwt_required()
def get_families_created():
    families_created = ctrl.get_families_created(current_user)
    return families_created


@bp.route("user/family/")
@jwt_required()
def get_user_family():
    family = ctrl.get_user_family(current_user.member)
    if family:
        return jsonify(family)
    return not_found("You don't have a family yet!")


@bp.route("user/<string:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    result = ctrl.delete_user_by_id(user_id)
    if not result:
        return not_found("User does not exist")
    return jsonify(result), 204


@bp.route("user/<string:user_id>/", methods=["PUT"])
@jwt_required()
def user_update(user_id):
    user = User.query.filter_by(id=user_id).one_or_none()
    updated_user = ctrl.update_user(user, request.json)
    if not updated_user:
        return not_found("User does not exist")
    return jsonify(updated_user)


@bp.route("user/family/", methods=["POST"])
@jwt_required()
def create_my_family():
    """Creates a family for the user"""
    role = request.json.get("role")
    member = Member.query.filter_by(user_id=current_user.id).one_or_none()
    if member:
        result, status_code = ctrl.handle_existing_member(
            member, role, request=request.json
        )
        if status_code == 400:
            return bad_request(result)
        return jsonify(result), status_code
    else:
        result, status_code = ctrl.handle_new_member(
            current_user, role, request=request.json
        )
        return jsonify(result), status_code
