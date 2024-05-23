from flask_jwt_extended import current_user, jwt_required
from app.api import api_v1_bp as fam_bp
from flask import jsonify, request
from app.api.errors import bad_request, not_found
from app.api.v1.controllers import family_member_controller as ctrl


@fam_bp.route("family/<string:_id>/", methods=["GET"])
@jwt_required()
def get_family(_id):
    family_by_member_id = ctrl.fetch_family_by_member_id(_id)
    if family_by_member_id:
        return jsonify(family_by_member_id.to_dict()), 200

    family_by_fam_id = ctrl.fetch_family_by_fam_id(_id)
    if family_by_fam_id:
        return jsonify(family_by_fam_id.to_dict()), 200
    return not_found("Family does not exist")


@fam_bp.route("family/members/<string:family_id>/", methods=["GET"])
@jwt_required()
def get_family_members(family_id):
    family_members = ctrl.fetch_family_members(family_id)
    if not family_members:
        return not_found("Family has no members")
    return jsonify(family_members), 200


@fam_bp.route("family/member/get-siblings/<string:member_id>")
@jwt_required()
def get_siblings(member_id):
    member = ctrl.fetch_member(member_id)
    if not member:
        user = ctrl.fetch_user(member_id)
        if not user or not user.member:
            return not_found("member does not exist")
        member = user.member
    return jsonify(member.get_siblings()), 200


@fam_bp.route("family/member/<string:member_id>/", methods=["GET"])
@jwt_required()
def get_family_member(member_id):
    member = ctrl.fetch_member(member_id)
    if not member:
        member = current_user.member
        if not member:
            if member_id == current_user.id:
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
    ancestors = ctrl.fetch_ancestors(member_id, int(level))
    if not ancestors:
        return not_found("Member not found")
    return jsonify(ancestors), 200


@fam_bp.route("/family/descendants/<string:member_id>/", methods=["GET"])
@jwt_required()
def get_descendants(member_id):
    level = request.args.get("level")
    if not level:
        return bad_request("Level must be provide in request args")
    descendants = ctrl.fetch_descendants(member_id, int(level))
    if not descendants:
        return not_found("member does not exist")
    return jsonify(descendants)


@fam_bp.route("/family/owner/<string:family_id>")
@jwt_required()
def get_family_owner(family_id):
    family = ctrl.fetch_family_owner(family_id)
    if not family:
        return not_found("Family does not exist")
    return family.creator.basic_info_dict()


@fam_bp.route("/family/", methods=["POST"])
@jwt_required()
def make_family():
    family = ctrl.create_family(current_user.id, request.json)
    return family.to_dict(), 201


@fam_bp.route("family/member/<string:family_id>/", methods=["POST"])
@jwt_required()
def create_family_member(family_id):
    new_member = ctrl.create_family_member(family_id, request.json)
    if not new_member:
        return not_found("Family not found")
    return new_member.to_dict(family_id), 201


@fam_bp.route("family/<string:family_id>/", methods=["PUT"])
@jwt_required()
def update_family(family_id):
    family = ctrl.update_family(family_id, request.json)
    if not family:
        return not_found("Family not found")
    return family.to_dict(), 200


@fam_bp.route("family/member/<string:member_id>/", methods=["PUT"])
@jwt_required()
def update_family_member(member_id):
    member = ctrl.fetch_member(member_id)
    if not member:
        member = current_user.member
        if not member:
            return not_found("Member not found")
    member = ctrl.update_family_member(member, request.json)
    return member.to_dict(), 200


@fam_bp.route("family/<string:family_id>/", methods=["DELETE"])
@jwt_required()
def delete_family(family_id):
    family_dict = ctrl.delete_family(family_id)
    if not family_dict:
        return not_found("Family does not exist")
    return family_dict, 200


@fam_bp.route(
    "family/member/<string:family_id>/<string:member_id>/", methods=["DELETE"]
)
@jwt_required()
def delete_family_member(family_id, member_id):
    member_dict = ctrl.delete_family_member(family_id, member_id)
    if not member_dict:
        return not_found("Family or member not found")
    return jsonify(member_dict), 200


@fam_bp.route("family/members/<string:family_id>/", methods=["DELETE"])
@jwt_required()
def delete_family_members(family_id):
    family_members = ctrl.delete_family_members(family_id)
    if not family_members:
        return not_found("Family does not exist")
    return "", 204
