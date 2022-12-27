import wx
import requests

from packaging import version
from elmedievo_mods_app.common import *
from elmedievo_mods_app.startup import *


def mods_update_available(button, text):
    r = requests.get(f"{ELMEDIEVO_MODS_URL}/rva_data.json")

    if r.status_code != 200:
        print(f"Unable to retrieve ModPack update. Error {r.status_code}.")
        wx.CallAfter(text.SetLabelText, f"Unable to retrieve ModPack info.")
        return

    v = r.json()["version"]
    if version.parse(v) > version.parse(get_modpack_version()):
        wx.CallAfter(button.Enable)
        wx.CallAfter(text.SetLabelText, f"ModPack v{v} is available!")
        print(f"New ModPack version detected: {v}")
    else:
        wx.CallAfter(text.SetLabelText, f"ModPack is up to date.")
        wx.CallAfter(button.Disable)
        print(f"ModPack is up to date.")
