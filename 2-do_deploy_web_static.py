#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static """
from datetime import datetime
from fabric.api import local, run, env, put
import os

env.hosts = ['35.237.225.4', '34.74.173.192']
env.user = "ubuntu"


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

def do_deploy(archive_path):
    """creates/distributes an archive to web servers, using the deploy"""
    if (os.path.exists(archive_path)):
        try:
            path = archive_path.split('/')[1]
            no_ext = path.split('.')[0]
            data = "/data/web_static/releases/" + no_ext + "/"
            put(archive_path, "/tmp/")
            run("mkdir -p {}".format(data))
            run("tar -xzf /tmp/{} -C {}".format(path, data))
            run("rm /tmp/{}".format(path))
            run("mv {}web_static/* {}".format(data, data))
            run("rm -rf {}web_static".format(data))
            run("rm -rf /data/web_static/current")
            run("ln -s {} /data/web_static/current".format(data))
            return True
        except Exception:
            return False
    else:
        return False
