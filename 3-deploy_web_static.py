#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive of the npm build to the web servers
"""

# Import necessary modules from Fabric
from fabric.api import env, local, put, run
# Import datetime for timestamping archives
from datetime import datetime
# Import exists and isdir from os.path to check file/directory existence
from os.path import exists, isdir

env.key_filename ='./0-RSA'
# Define the hosts for Fabric
env.hosts = ['54.172.4.252', '54.175.109.84']

def do_pack():
    """
    Generates a .tgz archive of the npm build located in the frontend/dist directory.
    The archive is stored in the versions/ directory with a timestamp in its name.
    """
    try:
        # Get the current date and time in the format YYYYMMDDHHMMSS
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        # If the versions/ directory does not exist, create it
        if isdir("versions") is False:
            local("mkdir versions")
        # Define the name of the archive file
        file_name = "versions/npm_build_{}.tgz".format(date)
        # Create a .tgz archive of the npm build
        local("tar -cvzf {} frontend/dist".format(file_name))
        # Return the name of the archive file
        return file_name
    except:
        # If an error occurs, return None
        return None

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    The archive is extracted to the /var/www/unity-tree/releases/ directory.
    A symbolic link to the extracted archive is created at /var/www/unity-tree/current.
    """
    # Check if the archive file exists
    if exists(archive_path) is False:
        return False
    try:
        # Get the name of the archive file
        file_n = archive_path.split("/")[-1]
        # Get the name of the archive file without the extension
        no_ext = file_n.split(".")[0]
        # Define the path to the releases directory
        path = "/var/www/unity-tree/releases/"
        # Upload the archive to the /tmp directory on the web server
        put(archive_path, '/tmp/')
        # Create a new directory for the archive in the releases directory
        run('mkdir -p {}{}/'.format(path, no_ext))
        # Extract the archive to the new directory
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        # Remove the archive from the /tmp directory
        run('rm /tmp/{}'.format(file_n))
        # Move the contents of the npm_build directory to the parent directory
        run('mv {0}{1}/npm_build/* {0}{1}/'.format(path, no_ext))
        # Remove the now empty npm_build directory
        run('rm -rf {}{}/npm_build'.format(path, no_ext))
        # Remove the current symbolic link
        run('rm -rf /var/www/unity-tree/current')
        # Create a new symbolic link to the new directory
        run('ln -s {}{}/ /var/www/unity-tree/current'.format(path, no_ext))
        # Return True if the deployment was successful
        return True
    except:
        # If an error occurs, return False
        return False

def deploy():
    """
    Creates and distributes an archive to the web servers.
    This function calls do_pack to create the archive and do_deploy to distribute it.
    """
    # Call do_pack to create the archive
    archive_path = do_pack()
    # If do_pack returned None (i.e., the archive was not created), return False
    if archive_path is None:
        return False
    # Call do_deploy to distribute the archive and return its result
    return do_deploy(archive_path)
