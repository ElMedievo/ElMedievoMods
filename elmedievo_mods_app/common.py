import os
import sys
import platform
import requests
import threading

# GUI Constants

APP_NAME = "elmedievoapp"
APP_TITLE = "ElMedievo Mods"
APP_TITLE_WITH_VER = 'ElMedievo Mods'
APP_MIN_SIZE = (960, 640)
APP_MAX_SIZE = (960, 640)
APP_SIZE = (960, 640)
ELMEDIEVO_MODS_URL = "https://distribute.elmedievo.org/mods"
CONFIG_DIR = os.curdir

close_event = threading.Event()
close_event.clear()

message_event = threading.Event()
message_event.clear()

session = requests.Session()
item = 0

if sys.platform == "linux":
    PLATFORM = "linux"
elif sys.platform == "win32":
    if platform.architecture()[0] == "64bit":
        PLATFORM = "win64"
    else:
        PLATFORM = "win32"
elif sys.platform == "darwin":
    PLATFORM = "macos"


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
