import os

from elmedievo_mods_app import CONFIG_DIR
from elmedievo_mods_app.elmedievo_gui.widgets import *


class ModsTab(ScrolledTabPage):
    def __init__(self, parent):
        TabPage.__init__(self, parent)
        self.init_ui()

    def init_ui(self):
        self.box = wx.BoxSizer(wx.VERTICAL)

        # Repository List
        widths = [180, 420, 160]
        self.list = CheckListCtrl(self, widths, -1, style=wx.LC_REPORT)
        self.list.InsertColumn(0, "Name", width=widths[0])
        self.list.InsertColumn(1, "Status", width=widths[1])
        self.list.InsertColumn(2, "Required", width=widths[2])

        self.list.Bind(EVT_LIST_ITEM_CHECKED, self.on_toggled)
        self.list.Bind(EVT_LIST_ITEM_UNCHECKED, self.on_toggled)

        # Main toolbar
        self.box_toolbar = wx.BoxSizer(wx.HORIZONTAL)
        self.button_update_info = wx.Button(self, -1, "Update Mod Info")
        self.button_update_info.Bind(wx.EVT_BUTTON, self.refresh_mods)
        self.box_toolbar.Add(self.button_update_info, 1, wx.EXPAND | wx.ALL, 5)

        # Controls toolbar
        self.box_controls = wx.BoxSizer(wx.HORIZONTAL)
        self.mods_install_button = wx.Button(self, label="Install")
        self.mods_install_button.Bind(wx.EVT_BUTTON, self.on_mods_install)

        self.box_controls.Add(self.mods_install_button, 1, wx.EXPAND | wx.ALL, 5)

        self.box.Add(self.box_toolbar, 0, wx.EXPAND)
        self.box.Add(self.list, 1, wx.EXPAND)
        self.box.Add(self.box_controls, 0, wx.EXPAND)

        self.list.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.on_double_click)
        self.list.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_selected)
        self.list.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.on_selected)

        self.SetSizer(self.box)
        self.refresh_mods()

    def on_toggled(self, e):
        self.refresh_mods()

    def on_mods_install(self, e):
        pass

    def refresh_mods(self):
        pos = self.list.get_scroll_pos()
        self.list.DeleteAllItems()

        item = 0
        for f in os.listdir(os.path.join(CONFIG_DIR, "mods")):
            self.list.InsertItem(item, f)
            self.list.SetItem(item, 1, "Installed")
            self.list.SetItem(item, 2, "Yes")

            # Everything in 'mods/' is required
            self.list.CheckItem(item, check=True, event=False)
            item += 1

        for f in os.listdir(os.path.join(CONFIG_DIR, "mods_opt")):
            self.list.InsertItem(item, f)
            self.list.SetItem(item, 1, "Installed")
            self.list.SetItem(item, 2, "Yes")

            # Everything in 'mods_opt/' is NOT required
            self.list.CheckItem(item, check=False, event=False)
            item += 1

        self.Layout()
        self.list.set_column_widths()
        self.list.set_scroll_pos(pos)

        self.on_selected(None)

    def on_double_click(self, e):
        pass

    def on_selected(self, e):
        pass
