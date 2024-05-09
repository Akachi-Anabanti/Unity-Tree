from flask_jwt_extended import current_user, jwt_required
from app.api import api_v1_bp as fam_bp
from flask import jsonify, request
from app import models
from app.api.errors import bad_request, not_found
from app import db


# # static family data

# familyMembers = {
#     "father": {
#         "id": "random-father-id",
#         "name": "C-3PO",
#         "dateOfBirth": "2025-01-29",
#         "img": "https://randomuser.me/api/portraits/men/1.jpg",
#         "role": "parent",
#     },
#     "mother": {
#         "id": "random-mother-id",
#         "name": "Luke Skywalker",
#         "dateOfBirth": "2025-01-29",
#         "img": "https://randomuser.me/api/portraits/women/5.jpg",
#         "role": "parent",
#     },
#     "children": [
#         {
#             "id": "random-first-child-id",
#             "name": "Obi-Wan Kenobi",
#             "dateOfBirth": "2025-01-29",
#             "img": "https://randomuser.me/api/portraits/men/2.jpg",
#             "role": "child",
#         },
#         {
#             "id": "random-second-child-id",
#             "name": "Jabba Desilijic Tiure",
#             "dateOfBirth": "2025-02-24",
#             "img": "https://randomuser.me/api/portraits/women/4.jpg",
#             "role": "child",
#         },
#         {
#             "id": "random-third-child-id",
#             "name": "Darth Vader",
#             "dateOfBirth": "2025-04-20",
#             "img": "https://randomuser.me/api/portraits/men/6.jpg",
#             "role": "child",
#         },
#         {
#             "id": "random-last-child-id",
#             "name": "Obi-Wan Kenobi",
#             "dateOfBirth": "2025-04-20",
#             "img": "https://randomuser.me/api/portraits/men/2.jpg",
#             "role": "child",
#         },
#     ],
# }

# family = {
#     "id": "random-family-id",
#     "name": "Family Name",
#     "created_by": "random-owner-id",
# }


@fam_bp.route("family/<string:member_id>/", methods=["GET"])
@jwt_required()
def get_family(member_id):
    family = models.FamilyMember.get_family_by_member_id(member_id)
    if not family:
        return not_found("Member does not belong to a family")
    return jsonify(family.to_dict()), 200


@fam_bp.route("family/members/<string:family_id>/", methods=["GET"])
@jwt_required()
def get_family_members(family_id):
    family_members = models.Family.get_family_members(family_id)
    if not family_members:
        return not_found("Family has no members", 404)
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
    member = models.Member.query.get(member_id)
    decendants = member.get_decendants(level)
    return jsonify(decendants)


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
    db.session.delete(family)
    db.session.commit()


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
