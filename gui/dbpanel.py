import wx

from .dbview import DbView
from gui.locale import rus as locale


class DbPanel(wx.Panel):
    def __init__(self, parent, table, add_label):
        super(DbPanel, self).__init__(parent)

        self.table = table

        self.button_sizer = wx.BoxSizer(wx.VERTICAL)
        self.button_sizer.Add(self._get_view_buttons(add_label), 0)

        self.db_list = DbView(self, table)

        outer_sizer = wx.BoxSizer(wx.HORIZONTAL)

        outer_sizer.Add(self.db_list, 1, wx.EXPAND)
        outer_sizer.AddSpacer(4)
        outer_sizer.Add(self.button_sizer, 0, wx.EXPAND)

        self.SetSizer(outer_sizer)

    def _get_view_buttons(self, add_label):
        sizer = wx.GridSizer(2, 1, 10, 0)

        buttons = [wx.Button(self, label=add_label),
                   wx.Button(self, label=locale.DELETE_BUTTON)]

        for func, button in zip([self._on_add, self._on_delete], buttons):
            sizer.Add(button, 1, wx.EXPAND)
            self.Bind(wx.EVT_BUTTON, func, button)

        return sizer

    def _on_add(self, e):
        print('on add')

    def _on_delete(self, e):
        print('on delete')
