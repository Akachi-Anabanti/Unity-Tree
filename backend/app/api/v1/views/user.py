from app.api import api_v1_bp as bp
from flask import jsonify, request
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required
from app.api.errors import not_found, bad_request
from app.models import User, Family, Member, FamilyMember
from app import db


@bp.route("ping")
@jwt_required(optional=True)
def ping():
    return jsonify({"msg": "Pong"}), 200


@bp.route("user/")
@jwt_required()
def get_user():
    user = current_user.to_dict()
    return jsonify(user), 200


@bp.route("user/family-created/")
@jwt_required()
def get_families_created():
    return current_user.get_families_created()


@bp.route("user/family/")
@jwt_required()
def get_user_family():
    member = current_user.member
    if member:
        family = FamilyMember.get_family_by_member_id(member.id)
        if family:
            return family.to_dict()
    return not_found("You don't have a family yet!")


@bp.route("user/<string:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return not_found("User does not exist")
    db.session.delete(user)
    db.session.commit(), 204

    return jsonify({"msg": "successfully deleted"})


@bp.route("user/<string:user_id>/", methods=["PUT"])
@jwt_required()
def user_update(user_id):
    user = User.query.filter_by(id=user_id).one_or_none()

    if not user:
        return not_found("User does not exist")
    user.update_user(**request.json)
    user.member.update(**request.json)
    db.session.commit()

    return user.to_dict()


@bp.route("user/family/", methods=["POST"])
@jwt_required()
def create_my_family():
    """Creates a family for the user"""
    role = request.json.get("role")
    member = Member.query.filter_by(user_id=current_user.id).one_or_none()

    if member:
        return handle_existing_member(member, role)
    else:
        return handle_new_member(role)


def handle_existing_member(member, role):
    if role not in [family.role for family in member.families]:
        new_family = create_family(member, role)
        return new_family.to_dict(), 201
    else:
        return bad_request(f"You are already a {role} in a family!")


def handle_new_member(role):
    new_member = create_member()
    new_family = create_family(new_member, role)
    return new_family.to_dict(), 201


def create_member():
    new_member = Member(
        first_name=current_user.first_name,
        last_name=current_user.last_name,
        date_of_birth=current_user.date_of_birth,
    )
    new_member.user_id = current_user.id
    new_member.registered = True
    db.session.add(new_member)
    return new_member


def create_family(member, role):
    new_family = Family.create_family(current_user.id, **request.json)
    fam_member = FamilyMember().create_family_member(
        new_family.id, member.id, role=role
    )
    db.session.add_all([new_family, fam_member])
    db.session.commit()
    return new_family
