import os
import zipfile
import io
import json

from packaging import version
from elmedievo_mods_app.common import *
from elmedievo_mods_app.helpers import *

""" Makes sure all folders exist """
def prepare_folders():
    for folder in ["mods", "mods_opt"]:
        create_folder(os.path.join(CONFIG_DIR, folder))


""" Retrieves all the ModPack files and creates them if they don't exist """
def fetch_data():
    if mods_update_available():
        # Download and unpack mods.zip
        mods_file = "mods.zip"
        mods_zip_url = f"{ELMEDIEVO_MODS_URL}/{mods_file}"
        mods_target_dir = f"./mods/"

        r = requests.get(mods_zip_url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(mods_target_dir)

        # Download and unpack mods_opt.zip
        mods_opt_file = "mods_opt.zip"
        mods_opt_zip_url = f"{ELMEDIEVO_MODS_URL}/{mods_opt_file}"
        mods_opt_target_dir = f"./mods_opt/"

        r = requests.get(mods_opt_zip_url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(mods_opt_target_dir)


def mods_update_available():
    r = requests.get(f"{ELMEDIEVO_MODS_URL}/modpack.json")

    if r.status_code != 200:
        print(f"Unable to retrieve ModPack update. Error {r.status_code}.")
        return False

    v = r.json()["version"]
    if version.parse(v) > version.parse(get_modpack_version()):
        print(f"New ModPack version detected: {v}")
        create_file("modpack.json", r.text)
        return True
    else:
        print(f"ModPack is up to date.")
        return False


""" Retrieves the ModPack version string from its version file. If not found, a new modpack version file is downloaded. """
def get_modpack_version():
    data_version_file_path = os.path.join(os.getcwd(), "modpack.json")
    if not os.path.isfile(data_version_file_path):
        r = requests.get(f"{ELMEDIEVO_MODS_URL}/modpack.json")
        create_file(data_version_file_path, r.text)

    with open(data_version_file_path, "r") as f:
        data_version_json = json.load(f)

    return data_version_json["version"]


# FIXME: This was made in a rush! We need a better way of checking for some of these things...
def load_mods():
    item = 0

    # Everything in 'mods/' is required and checked by default
    for f in os.listdir(os.path.join(CONFIG_DIR, "mods")):
        mod = {
            "item": item,
            "name": f,
            "required": True,
            "checked": True
        }

        mods[f] = mod
        item += 1

    # Everything in 'mods_opt/' is NOT required and NOT checked by default
    for f in os.listdir(os.path.join(CONFIG_DIR, "mods_opt")):
        mod = {
            "item": item,
            "name": f,
            "required": False,
            "checked": True
        }

        mods[f] = mod
        item += 1
