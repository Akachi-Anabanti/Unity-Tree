from app.api import api_v1_bp as fam_bp
from flask import jsonify


# static family data

familyMembers = {
    "father": {
        "id": "random-father-id",
        "name": "C-3PO",
        "dateOfBirth": "2025-01-29",
        "img": "https://randomuser.me/api/portraits/men/1.jpg",
        "role": "parent",
    },
    "mother": {
        "id": "random-mother-id",
        "name": "Luke Skywalker",
        "dateOfBirth": "2025-01-29",
        "img": "https://randomuser.me/api/portraits/women/5.jpg",
        "role": "parent",
    },
    "children": [
        {
            "id": "random-first-child-id",
            "name": "Obi-Wan Kenobi",
            "dateOfBirth": "2025-01-29",
            "img": "https://randomuser.me/api/portraits/men/2.jpg",
            "role": "child",
        },
        {
            "id": "random-second-child-id",
            "name": "Jabba Desilijic Tiure",
            "dateOfBirth": "2025-02-24",
            "img": "https://randomuser.me/api/portraits/women/4.jpg",
            "role": "child",
        },
        {
            "id": "random-third-child-id",
            "name": "Darth Vader",
            "dateOfBirth": "2025-04-20",
            "img": "https://randomuser.me/api/portraits/men/6.jpg",
            "role": "child",
        },
        {
            "id": "random-last-child-id",
            "name": "Obi-Wan Kenobi",
            "dateOfBirth": "2025-04-20",
            "img": "https://randomuser.me/api/portraits/men/2.jpg",
            "role": "child",
        },
    ],
}

family = {
    "id": "random-family-id",
    "name": "Family Name",
    "created_by": "random-owner-id",
}


@fam_bp.route("family/members/<string:family_id>/", methods=["GET"])
def get_family_members(family_id):

    if family_id == family.get("id"):
        return jsonify(familyMembers), 200
    return jsonify({"message": "not found"}), 404


@fam_bp.route("family/<string:member_id>/", methods=["GET"])
def get_family(member_id):
    return jsonify(family), 200
