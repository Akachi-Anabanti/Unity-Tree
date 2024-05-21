from fabric import task
from fabric.connection import Connection
from datetime import datetime
from os.path import exists, isdir
import os
import invoke

env_hosts = ['54.172.4.252', '54.175.109.84']
key_filename = './0-RSA'

@task
def do_pack(c):
    """
    Generates a .tgz archive of the npm build located in the frontend/dist directory.
    The archive is stored in the versions/ directory with a timestamp in its name.
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            os.makedirs("versions")
        file_name = f"versions/npm_build_{date}.tgz"
        invoke.run(f"tar -cvzf {file_name} frontend/dist")
        return file_name
    except Exception as e:
        print(f"Error: {e}")
        return None

@task
def do_deploy(c, archive_path):
    """
    Distributes an archive to the web servers.
    The archive is extracted to the /var/www/unity-tree/releases/ directory.
    A symbolic link to the extracted archive is created at /var/www/unity-tree/current.
    """
    if not exists(archive_path):
        return False
    try:
        file_n = os.path.basename(archive_path)
        no_ext = file_n.split(".")[0]
        path = "/var/www/unity-tree/releases/"
        c.put(archive_path, '/tmp/')
        c.run(f'mkdir -p {path}{no_ext}/')
        c.run(f'tar -xzf /tmp/{file_n} -C {path}{no_ext}/')
        c.run(f'rm /tmp/{file_n}')
        c.run(f'mv {path}{no_ext}/frontend/dist/* {path}{no_ext}/')
        c.run(f'rm -rf {path}{no_ext}/frontend')
        c.run('rm -rf /var/www/unity-tree/current')
        c.run(f'ln -s {path}{no_ext}/ /var/www/unity-tree/current')
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

@task
def deploy(c):
    """
    Creates and distributes an archive to the web servers.
    This function calls do_pack to create the archive and do_deploy to distribute it.
    """
    archive_path = do_pack(c)
    if archive_path is None:
        return False
    for host in env_hosts:
        c = Connection(host, connect_kwargs={"key_filename":key_filename})
        if not do_deploy(c, archive_path):
            return False
        return True
    return do_deploy(c, archive_path)
