import os
from werkzeug.utils import secure_filename


class FileService:
    def __init__(self, upload_folder, allowed_extensions):
        self.upload_folder = upload_folder
        self.allowed_extensions = allowed_extensions

    def allowed_file(self, filename):
        return "." in filename and filename.rsplit(".", 1)[1] in self.allowed_extensions

    def save_file(self, file, family, member):
        # Create a directory for the family if it doesn't exist
        family_dir = os.path.join(self.upload_folder, family)
        os.makedirs(family_dir, exist_ok=True)
        # Create a directory for the member within the family directory if it doesn't exist
        member_dir = os.path.join(family_dir, member)
        os.makedirs(member_dir, exist_ok=True)
        # Check if the file is one of the allowed types/extensions
        if file and self.allowed_file(file.filename):
            # Make the filename safe, remove unsupported chars
            filename = secure_filename(file.filename)
            # Move the file from the temporal folder to the upload
            # folder we setup
            file.save(os.path.join(member_dir, filename))
            return True
        return False
