from flask_jwt_extended import jwt_required
from app import file_service
from app.api import api_v1_bp as md_bp
from flask import send_from_directory, jsonify, url_for
from werkzeug.utils import secure_filename
import os

from app.api.errors import bad_request, not_found
from app.config import Settings


@md_bp.route("/upload/<string:family_id>/<string:member_id>/", methods=["POST"])
@jwt_required()
def upload_file(family_id, member_id, file=None):
    """Defines a route that uploads a file to the server
    directory and returns the url of the file"""

    if file.filename == "":
        return bad_request("No selected file")
    if file and file_service.allowed_file(file.filename):
        if file_service.save_file(file, family=family_id, member=member_id):
            filename = secure_filename(file.filename)
            img_url = url_for(
                "api.serve_file",
                family_id=family_id,
                member_id=member_id,
                filename=filename,
                _external=True,
            )
            return jsonify({"msg": "File uploaded successfully", "url": img_url})
        return bad_request("file upload failed")
    return bad_request("File type not allowed")


@md_bp.route("/uploads/<string:family_id>/<string:member_id>/<string:filename>/")
@jwt_required()
def serve_file(family_id, member_id, filename):
    """Defines a route that serves image files"""
    family_dir = os.path.join(Settings.UPLOAD_FOLDER, family_id)
    member_dir = os.path.join(family_dir, member_id)

    try:
        return send_from_directory(member_dir, filename)
    except FileNotFoundError:
        return not_found("File not found")
