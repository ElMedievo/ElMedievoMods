import io
import json
import zipfile

from elmedievo_mods_app.common import *
from elmedievo_mods_app.helpers import *

""" Makes sure all folders exist """
def prepare_folders():
    for folder in ["mods", "mods_opt"]:
        create_folder(os.path.join(CONFIG_DIR, folder))


""" Retrieves all the ModPack files and creates them if they don't exist """
def fetch_data():
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


""" Retrieves the data version string from its version folder. If not found, a new data version file is downloaded. """
def get_modpack_version():
    data_version_file_path = os.path.join(os.getcwd(), "modpack.json")
    if not os.path.isfile(data_version_file_path):
        r = requests.get(f"{ELMEDIEVO_MODS_URL}/modpack.json")
        create_file(data_version_file_path, r.text)

    with open(data_version_file_path, "r") as f:
        data_version_json = json.load(f)

    return data_version_json["version"]