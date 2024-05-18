from datetime import datetime
from flask_jwt_extended import current_user, jwt_required
from app.api import api_v1_bp as fam_bp
from flask import jsonify, request
from app import models
from app.api.errors import bad_request, not_found
from app import db


@fam_bp.route("family/<string:_id>/", methods=["GET"])
@jwt_required()
def get_family(_id):
    family = get_family_by_member_id(_id) or get_family_by_family_id(_id)
    if family:
        return jsonify(family.to_dict()), 200
    else:
        return not_found("Family does not exist")


def get_family_by_member_id(member_id):
    return models.FamilyMember.get_family_by_member_id(member_id)


def get_family_by_family_id(family_id):
    return models.Family.query.get(family_id)


@fam_bp.route("family/members/<string:family_id>/", methods=["GET"])
@jwt_required()
def get_family_members(family_id):

    family_members = models.Family.get_family_members(family_id)
    if not family_members:
        return not_found("Family has no members")
    return jsonify(family_members), 200


@fam_bp.route("family/member/get-siblings/<string:member_id>")
@jwt_required()
def get_siblings(member_id):
    member = models.Member.query.get(member_id)
    if not member:
        user = models.User.query.get(member_id)
        if not user or not user.member:
            return not_found("member does not exist")
        member = user.member
    return jsonify(member.get_siblings()), 200


@fam_bp.route("family/member/<string:member_id>/", methods=["GET"])
@jwt_required()
def get_family_member(member_id):
    member = models.Member.query.get(member_id)
    if not member:
        # tries to retrieve current user as member
        member = current_user.member
        if not member:
            if member_id == current_user.id:
                # current user as current user similar to get current user
                # this should be seperated into the user line
                member = current_user
            else:
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
    family = models.Family.create_family(creator_id=current_user.id, **request.json)
    db.session.add(family)
    db.session.commit()
    return family.to_dict(), 201


@fam_bp.route("family/member/<string:family_id>/", methods=["POST"])
@jwt_required()
def create_family_member(family_id):
    data = validate_input(request.json)
    family = get_family(family_id)
    new_member = create_member(data, family)
    fam_member = create_family_member(family_id, new_member.id, data["role"])
    return new_member.to_dict(family_id), 201


def validate_input(data):
    required_fields = ["firstName", "lastName", "role", "dateOfBirth"]
    for field in required_fields:
        if field not in data:
            raise bad_request(f"{field} is required")
    return data


def get_family(family_id):
    family = models.Family.query.get(family_id)
    if not family:
        raise not_found("Family not found")
    return family


def create_member(data, family):
    date_of_birth = datetime.strptime(data["dateOfBirth"], "%Y-%m-%dT%H:%M:%S.%fZ")
    new_member = models.Member(
        first_name=data["firstName"], last_name=family.name, date_of_birth=date_of_birth
    )
    db.session.add(new_member)
    return new_member


def create_family_member(family_id, member_id, role):
    fam_member = models.FamilyMember().create_family_member(family_id, member_id, role)
    db.session.add(fam_member)
    db.session.commit()
    return fam_member


# UPDATE ROUTES
@fam_bp.route("family/<string:family_id>/", methods=["PUT"])
@jwt_required()
def update_family(family_id):
    family = models.Family.query.get(family_id)
    if not family:
        return not_found("Family not found")
    family.update_family(**request.json)
    db.session.commit()
    return family, 200


@fam_bp.route("family/member/<string:member_id>/", methods=["PUT"])
@jwt_required()
def update_family_member(member_id):
    member = models.Member.query.get(member_id)
    if not member:
        return not_found("Member not found")

    member.update_member(**request.json)
    db.session.commit()
    return member.basic_info_dict(), 200


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
    return family_dict, 200


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
    return jsonify(member_dict), 200


@fam_bp.route("family/members/<string:family_id>/", methods=["DELETE"])
@jwt_required()
def delete_family_members(family_id):

    family = models.Family.query.get(family_id)
    if not family:
        return not_found("Family does not exist")
    family_members = models.FamilyMember.delete_family_members(family_id)
    for member in family_members:
        db.session.delete(member)
    db.session.commit(), 204


#
# services.py
# from datetime import datetime
# from app import models, db

# def get_family_by_member_id(member_id):
#     return models.FamilyMember.get_family_by_member_id(member_id)

# def get_family_by_family_id(family_id):
#     return models.Family.query.get(family_id)

# def create_family(creator_id, data):
#     family = models.Family.create_family(creator_id=creator_id, **data)
#     db.session.add(family)
#     db.session.commit()
#     return family

# ... and so on for the rest of the functions
