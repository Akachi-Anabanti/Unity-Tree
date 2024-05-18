import uuid
from flask import Flask, jsonify, request, send_from_directory, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# This is the path to the upload directory
app.config["UPLOAD_FOLDER"] = "static/uploads/"
# These are the extension that we are accepting to be uploaded
app.config["ALLOWED_EXTENSIONS"] = {"png", "jpg", "jpeg", "gif"}


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1] in app.config["ALLOWED_EXTENSIONS"]
    )


@app.route("/upload", methods=["POST"])
def upload():
    # Get the name of the uploaded file
    file = request.files["file"]
    # Get the family and member from the form data
    family = request.form.get("family")
    member = request.form.get("member")
    # Create a directory for the family if it doesn't exist
    family_dir = os.path.join(app.config["UPLOAD_FOLDER"], family)
    os.makedirs(family_dir, exist_ok=True)
    # Create a directory for the member within the family directory if it doesn't exist
    member_dir = os.path.join(family_dir, member)
    os.makedirs(member_dir, exist_ok=True)
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file from the temporal folder to the upload
        # folder we setup
        file.save(os.path.join(member_dir, filename))
        # Redirect the user to the uploaded_file route, which
        # will basically show on the browser the uploaded file
        return "File uploaded successfully"


@app.route("/uploads/<family>/<member>/<filename>")
def uploaded_file(family, member, filename):
    return send_from_directory(
        os.path.join(app.config["UPLOAD_FOLDER"], family, member), filename
    )


@app.route("/uploads/<family>/<member>", methods=["GET"])
def list_files(family, member):
    # Create the path to the member's directory
    member_dir = os.path.join(app.config["UPLOAD_FOLDER"], family, member)
    # Get a list of all files in the directory
    files = os.listdir(member_dir)
    # Create a list of urls for each file
    file_urls = [
        url_for(
            "uploaded_file", family=family, member=member, filename=f, _external=True
        )
        for f in files
    ]
    # Return the list of file urls
    return jsonify(file_urls)
