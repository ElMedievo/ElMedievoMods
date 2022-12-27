import os
import sys
import wx
import webbrowser

from elmedievo_mods_app.common import *
from elmedievo_mods_app.startup import prepare_folders
from elmedievo_mods_app.startup import fetch_data
from elmedievo_mods_app.elmedievo_gui.tabs import ModsTab
from elmedievo_mods_app.elmedievo_gui.widgets import TabBar


class FrameMain(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(FrameMain, self).__init__(*args, **kwargs)

        self.init_ui()

    def on_size(self):
        self.Layout()

    def init_ui(self):
        self.SetTitle(APP_TITLE_WITH_VER)
        self.set_icon()

        self.SetMinSize(APP_MIN_SIZE)
        self.SetMaxSize(APP_MAX_SIZE)
        self.SetSize(APP_SIZE)
        self.Center()

        self.box = wx.BoxSizer(wx.VERTICAL)

        self.tab_bar = TabBar(self)
        self.mods_tab = ModsTab(self.tab_bar)

        self.tab_bar.AddPage(self.mods_tab, "Mods")

        self.box.Add(self.tab_bar, 1, wx.EXPAND, 0)
        self.SetSizer(self.box)

        self.init_menubar()

    def init_menubar(self):
        self.menu_bar = wx.MenuBar()

        " File "
        self.menu_files = wx.Menu()

        self.menu_files_quit = self.menu_files.Append(wx.ID_EXIT, "Quit", "Quit application")
        self.Bind(wx.EVT_MENU, self.on_quit, self.menu_files_quit)

        self.menu_bar.Append(self.menu_files, "&File")

        " Help "
        self.menu_help = wx.Menu()
        self.menu_help_report_bug = self.menu_help.Append(-1, "Report a Bug", "Opens our GitHub Issues page")
        self.Bind(wx.EVT_MENU, self.on_report_a_bug, self.menu_help_report_bug)

        self.menu_bar.Append(self.menu_help, "&Help")

        self.SetMenuBar(self.menu_bar)

    def on_quit(self, e):
        self.Close()
        e.Skip()

    def on_report_a_bug(self, e):
        webbrowser.open("https://github.com/ElMedievo/ElMedievoMods/issues")

    def set_icon(self):
        ext = ("png", "ico")[sys.platform == "win32"]
        icon_file = os.path.join("icons", f"icon.{ext}")
        if os.path.isfile(icon_file):
            self.SetIcon(wx.Icon(icon_file))


def main():
    app = wx.App()

    prepare_folders()
    fetch_data()

    app.SetAppName(APP_NAME)
    app.SetAppDisplayName(APP_TITLE)
    app.SetClassName(APP_TITLE)

    frame = FrameMain(None)
    frame.Show()

    app.SetTopWindow(frame)
    app.MainLoop()


if __name__ == '__main__':
    main()
