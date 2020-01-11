#!/usr/bin/python3
"""Fabric script generates .tgz archive from the contents of the web_static"""
from datetime import datetime
from fabric.operations import local
import os


def do_pack():
    """ generates a .tgz archive from the contents of the web_static """
    try:
        if not os.path.exists('./versions'):
            os.makedirs('./versions')

        datenow = datetime.now()

        time = datenow.strftime("%Y%m%d%H%M%S")

        local("tar -cvzf versions/web_static_{}.tgz web_static".format(time))

        return "versions/web_static_{}.tgz".format(time)

    except:
        return None
