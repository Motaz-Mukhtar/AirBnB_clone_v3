#!/usr/bin/python3
""" Write Fabric script that generates a .tgz
  archive from the contents of the web_static
  folder of AirBnB Clone repo, using the
  Function do_pack.
"""
import os.path
from datetime import datetime
from fabric.api import local
from fabric.api import run
from fabric.api import env
from fabric.api import put
env.hosts = ['54.210.177.146', '54.209.56.145']


def do_pack():
    """ All Files in the folder web_static
        will be added to the final archive"""
    date = datetime.utcnow()
    f = "versions/web_static_{}{}{}{}{}{}.tgz".format(date.year,
                                                      date.month,
                                                      date.day,
                                                      date.hour,
                                                      date.minute,
                                                      date.second)
    if os.path.isfile("versions") is False:
        if local("mkdir -p versions") is True:
            return None
    if local("tar -cvzf {} web_static".format(f)) is True:
        return None
    return f


def do_deploy(archive_path):
    """
        Distributes an archive to the web servers
    """
    if archive_path is None:
        return False
    file = archive_path.split('/')[-1]
    file_name = file.split('.')[0]
    if put(archive_path, '/tmp/{}'.format(file)) is False:
        return False
    if run("mkdir -p /data/web_static/releases/{}".
            format(file_name)) is False:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".
            format(file, file_name)) is False:
        return False
    if run("rm -r /tmp/{}".format(file)) is False:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".
            format(file_name, file_name)) is False:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
            format(file_name)) is False:
        return False
    if run("rm -rf /data/web_static/current") is False:
        return False
    if run("ln -s /data/web_static/releases/{} /data/web_static/current".
            format(file_name)) is False:
        return False
    return True


def deploy():
    """
        Creates and destributes an archive to your web servers
    """
    file = do_pack()
    if file is None:
        return False

    value = do_deploy(file)
    return value
