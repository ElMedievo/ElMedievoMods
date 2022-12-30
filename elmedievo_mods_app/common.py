import os
import sys
import platform
import requests

from appdirs import *

# GUI Constants

APP_NAME = "elmedievoapp"
APP_TITLE = "ElMedievo Mods"
APP_TITLE_WITH_VER = 'ElMedievo Mods'
APP_MIN_SIZE = (960, 640)
APP_MAX_SIZE = (960, 640)
APP_SIZE = (960, 640)
ELMEDIEVO_MODS_URL = "https://distribute.elmedievo.org/mods"
CONFIG_DIR = os.curdir

# FIXME: Check for multi-platform support
#       https://pypi.org/project/appdirs/

session = requests.Session()
mods = {} # TODO: Make this persistent

# FIXME: Only Windows path is known to be correct. Check the others
if sys.platform == "linux":
    PLATFORM = "linux"
    MINECRAFT_DIR = f"{user_data_dir(roaming=True)}/.minecraft"
elif sys.platform == "win32":
    if platform.architecture()[0] == "64bit":
        PLATFORM = "win64"
    else:
        PLATFORM = "win32"

    MINECRAFT_DIR = f"{user_data_dir(roaming=True)}\.minecraft"
elif sys.platform == "darwin":
    PLATFORM = "macos"
    MINECRAFT_DIR = f"{user_data_dir(roaming=True)}/.minecraft"


""" Returns whether application is run from a frozen bundle """
def is_frozen():
    return getattr(sys, "frozen", False)

""" Returns the application base folder """
def get_app_path():
    if is_frozen():
        return os.path.dirname(sys.executable)
    else:
        return sys.path[0]

""" Returns the path to assets bundled with the application """
def get_dist_path():
    if sys.platform == "win32" and not is_frozen():
        return os.path.join("dist", PLATFORM)
    else:
        return ""
