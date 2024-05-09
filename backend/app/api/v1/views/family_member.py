from flask_jwt_extended import current_user, jwt_required
from app.api import api_v1_bp as fam_bp
from flask import jsonify, request
from app import models
from app.api.errors import bad_request, not_found
from app import db


@fam_bp.route("family/<string:_id>/", methods=["GET"])
@jwt_required()
def get_family(_id):

    # Try fetching the family by testing the _id as member id
    family_by_member_id = models.FamilyMember.get_family_by_member_id(_id)
    if family_by_member_id:
        return jsonify(family_by_member_id.to_dict()), 200

    # if it fails try fetching the family by testing _id as family id
    family_by_fam_id = models.Family.query.get(_id)
    if family_by_fam_id:
        return jsonify(family_by_fam_id.to_dict()), 200
    return not_found("Family does not exist")


@fam_bp.route("family/members/<string:family_id>/", methods=["GET"])
@jwt_required()
def get_family_members(family_id):

    family_members = models.Family.get_family_members(family_id)
    if not family_members:
        return not_found("Family has no members")
    return jsonify(family_members), 200


@fam_bp.route("family/member/<string:member_id>/", methods=["GET"])
@jwt_required()
def get_family_member(member_id):
    member = models.FamilyMember.get_family_member(member_id)
    if not member:
        return not_found("member not found")
    return jsonify(member.to_dict()), 200


@fam_bp.route("family/ancestors/<string:member_id>/", methods=["GET"])
@jwt_required()
def get_ancestors(member_id):
    level = request.args.get("level")
    if not level:
        return bad_request("Level must be provide in request args")
    level = int(level)
    member = models.Member.query.get(member_id)

    if not member:
        return not_found("Member not found")

    ancestors = member.get_ancestors(level)

    return jsonify(ancestors), 200


@fam_bp.route("/family/decendants/<string:member_id>/", methods=["GET"])
@jwt_required()
def get_decendants(member_id):
    level = request.args.get("level")
    if not level:
        return bad_request("Level must be provide in request args")
    level = int(level)
    member = models.Member.query.get(member_id)
    if not member:
        return not_found("member does not exist")
    decendants = member.get_decendants(level)
    print(decendants)
    return jsonify(decendants)


@fam_bp.route("/family/owner/<string:family_id>")
@jwt_required()
def get_family_owner(family_id):
    family = models.Family.query.get(family_id)
    if not family:
        return not_found("Family does not exist")
    return family.creator.basic_info_dict()


# CREATE ROUTES


@fam_bp.route("/family/", methods=["POST"])
@jwt_required()
def make_family():
    name = request.json.get("name")
    family = models.Family.create_family(name=name, creator_id=current_user.id)
    db.session.add(family)
    db.session.commit()
    return family.to_dict()


@fam_bp.route("family/member/<string:family_id>/", methods=["POST"])
@jwt_required()
def create_family_member(family_id):

    first_name = request.json.get("first_name")
    last_name = request.json.get("last_name")
    role = request.json.get("role")

    new_member = models.Member(first_name=first_name, last_name=last_name)
    db.session.add(new_member)
    fam_member = models.FamilyMember().create_family_member(
        family_id, new_member.id, role
    )
    db.session.add(fam_member)
    db.session.commit()
    print(fam_member.to_dict())
    return fam_member.to_dict()


# UPDATE ROUTES
@fam_bp.route("family/<string:family_id>/", methods=["PUT"])
@jwt_required()
def update_family(family_id):
    family = models.Family.query.get(family_id)
    if not family:
        return not_found("Family not found")
    family.update_family(**request.json)
    db.session.commit()
    return family


@fam_bp.route("family/member/<string:member_id>/", methods=["PUT"])
@jwt_required()
def update_family_member(member_id):
    member = models.Member.query.get(member_id)
    if not member:
        return not_found("Member not found")

    member.update_member(**request.json)
    db.session.commit()
    return member.basic_info_dict()


# DELETE ROUTES
@fam_bp.route("family/<string:family_id>/", methods=["DELETE"])
@jwt_required()
def delete_family(family_id):
    family = models.Family.query.get(family_id)
    if not family:
        return not_found("Family does not exist")
    family_dict = family.to_dict()
    db.session.delete(family)
    db.session.commit()
    return family_dict


@fam_bp.route(
    "family/member/<string:family_id>/<string:member_id>/", methods=["DELETE"]
)
@jwt_required()
def delete_family_member(family_id, member_id):

    member = models.FamilyMember.delete_family_member(family_id, member_id)
    if not member:
        return not_found("Family or member not found")
    member_dict = member.to_dict()
    db.session.delete(member)
    db.session.commit()
    return jsonify(member_dict)


@fam_bp.route("family/members/<string:family_id>/", methods=["DELETE"])
@jwt_required()
def delete_family_members(family_id):

    family = models.Family.query.get(family_id)
    if not family:
        return not_found("Family does not exist")
    family_members = models.FamilyMember.delete_family_members(family_id)
    for member in family_members:
        db.session.delete(member)
    db.session.commit()
