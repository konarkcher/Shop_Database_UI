import enum

import wx

import model
from .locale import rus as locale


@enum.unique
class Ok(enum.Enum):
    Sqlite = enum.auto()
    Postgres = enum.auto()


class SqliteTab(wx.Panel):
    def __init__(self, parent):
        super(SqliteTab, self).__init__(parent)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(wx.StaticText(self, label=locale.FILE), 0,
                  wx.RIGHT | wx.LEFT, border=1)

        self.path_ctrl = wx.TextCtrl(self)
        sizer.Add(self.path_ctrl, 1)

        self.SetSizer(sizer)


class DbSetDial(wx.Dialog):
    def __init__(self, parent):
        super(DbSetDial, self).__init__(parent)

        panel = wx.Panel(self)
        notebook = wx.Notebook(panel)

        notebook.AddPage(SqliteTab(notebook), locale.SQLITE_DB)

        sizer = wx.BoxSizer()
        sizer.Add(notebook, 1, wx.EXPAND)
        panel.SetSizer(sizer)

        self.SetSize((300, 200))
        self.SetTitle(locale.SET_DB)
