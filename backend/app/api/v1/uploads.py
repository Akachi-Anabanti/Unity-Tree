import uuid
from flask import Flask, request, send_from_directory
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
    # Generate a unique user_id
    user_id = str(uuid.uuid4())
    # Create a directory for the user if it doesn't exist
    user_dir = os.path.join(app.config["UPLOAD_FOLDER"], user_id)
    os.makedirs(user_dir, exist_ok=True)
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file from the temporal folder to the upload
        # folder we setup
        file.save(os.path.join(user_dir, filename))
        # Redirect the user to the uploaded_file route, which
        # will basically show on the browser the uploaded file
        return "File uploaded successfully"


@app.route("/uploads/<user_id>/<filename>")
def uploaded_file(user_id, filename):
    return send_from_directory(
        os.path.join(app.config["UPLOAD_FOLDER"], user_id), filename
    )
