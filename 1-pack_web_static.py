#!/usr/bin/python3
""" Write Fabric script that generates a .tgz
  archive from the contents of the web_static
  folder of AirBnB Clone repo, using the
  Function do_pack.
"""
import os.path
from datetime import datetime
from fabric.api import local


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
        if local("mkdir -p versions") is False:
            return None
    if local("tar -cvzf {} web_static".format(f)) is False:
        return None
    return f
