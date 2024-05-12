from flask import request
import app.models as models
from app.api.errors import Unauthorized, not_found
from app.api import api_v1_bp
from flask import jsonify

from datetime import datetime
from datetime import timedelta
from datetime import timezone


# import requests
# from flask_sse import sse


from email_validator import validate_email, EmailNotValidError

from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
    set_access_cookies,
    unset_jwt_cookies,
)

from app import jwt
from app import db


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]

    return models.User.query.filter_by(id=identity).one_or_none()


@api_v1_bp.after_request
def refresh_expiring_jwts(response):

    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            user = models.User.query.get(get_jwt_identity())
            access_token = create_access_token(identity=user)
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # where there is no valid JWT. Just return the original response
        return response


def is_email_valid(email, **kwargs):
    try:
        validate_email(email, **kwargs)
        return True
    except EmailNotValidError as e:
        return False


@api_v1_bp.route("/login", methods=["POST"])
def login():
    response = jsonify({"message": "login successful"})

    payload = request.json

    email = payload.get("email")
    password = payload.get("password")

    user = models.User.query.filter_by(email=email).one_or_none()

    if not user or not user.validate_password(password) or not is_email_valid(email):
        return Unauthorized("Invalid email or password")

    access_token = create_access_token(identity=user)
    set_access_cookies(response, access_token)
    return response


@api_v1_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    response = jsonify({"message": "logout successful"})
    unset_jwt_cookies(response)
    return response


@api_v1_bp.route("/register", methods=["POST"])
def register():
    """registers the user"""

    username = request.json.get("username")
    email = request.json.get("email")
    password = request.json.get("password")

    if not is_email_valid(email, check_deliverability=True):
        return Unauthorized("email is not valid, please use a valid email address")

    new_user = models.User().create_user(
        username=username, email=email, password=password
    )
    if new_user is None:
        response = jsonify({"message": "User already exists"})
        return response, 204

    db.session.add(new_user)
    db.session.commit()
    response = jsonify({"message": "Registeration successfuly"})
    return response, 201


@api_v1_bp.route("/register/<string:member_id>", methods=["POST"])
def register_member(member_id):
    """Registers an already existing member,
    makes a member a user.
    """

    member = models.Member.query.filter_by(id=member_id).one_or_none()
    if not member:
        return not_found("Member does not exist")

    username = request.json.get("username")
    email = request.json.get("email")
    password = request.json.get("password")

    new_user = models.User.create_user(
        username=username, email=email, password=password
    )

    if new_user is None:
        response = jsonify({"message": "User already exists"})
        return response, 204

    member.user = new_user
    member.registered = True
    db.session.commit()

    return jsonify({"message": "Member registered successfully!"})


@api_v1_bp.route("/status/")
def api_status():
    return {"status": "online"}, 200


# @api_v1_bp.route("/stream")
# def stream():
#     status = "online"
#     sse.publish({"status": status}, type="api_status")
