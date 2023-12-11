#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['54.144.147.222', '34.202.164.9']


def do_clean(number=0):
    """out-of-date archives deletion.

    Args:
        number (int): The number to keep of archives.

    If number is 0 or 1, keeps the most recent archive. If
    number is 2, keeps the most and second-most recent...
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
