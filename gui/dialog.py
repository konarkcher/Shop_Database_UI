import enum

import wx

import model
from .locale import rus as locale


@enum.unique
class Ok(enum.Enum):
    SqliteSave = enum.auto()
    SqliteOpen = enum.auto()
    Postgres = enum.auto()


class SqliteTab(wx.Panel):
    def __init__(self, parent):
        super(SqliteTab, self).__init__(parent)

        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        top_sizer.Add(wx.StaticText(self, label=locale.FILE),
                      0, wx.LEFT, border=1)

        self.path_ctrl = wx.TextCtrl(self)
        top_sizer.Add(self.path_ctrl, 1)

        open_btn = wx.Button(self, label='...', size=(30, -1))
        save_btn = wx.Button(self, label='+', size=(30, -1))
        for btn in [open_btn, save_btn]:
            top_sizer.Add(btn, 0, wx.LEFT | wx.TOP, border=1)

        bottom_sizer = wx.GridSizer(1, 2, 2, 0)  # rows, cols, vgap, hgap

        accept_btn = wx.Button(self, label=locale.ACCEPT)
        cancel_btn = wx.Button(self, label=locale.CANCEL)
        for btn in [accept_btn, cancel_btn]:
            bottom_sizer.Add(btn, 1, wx.EXPAND)

        outer_sizer = wx.BoxSizer(wx.VERTICAL)

        outer_sizer.Add(top_sizer, 1, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND)
        outer_sizer.Add(bottom_sizer, 1, wx.BOTTOM | wx.EXPAND)

        self.SetSizer(outer_sizer)


class DbSetDial(wx.Dialog):
    def __init__(self, parent):
        super(DbSetDial, self).__init__(parent)

        panel = wx.Panel(self)
        notebook = wx.Notebook(panel)

        notebook.AddPage(SqliteTab(notebook), locale.SQLITE_DB)

        sizer = wx.BoxSizer()
        sizer.Add(notebook, 1, wx.EXPAND)
        panel.SetSizer(sizer)

        self.SetSize((400, 150))
        self.SetTitle(locale.SET_DB)
