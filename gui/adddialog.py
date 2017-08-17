import wx

from .locale import rus as locale


class CenterText(wx.StaticText):
    def __init__(self, parent, label=''):
        super(CenterText, self).__init__(parent, label=label,
                                         style=wx.ALIGN_CENTER)


class AddDialog(wx.Dialog):
    def __init__(self, parent, title, column_list, source):
        super(AddDialog, self).__init__(parent, title=title)

        input_sizer = wx.FlexGridSizer(2 * len(column_list), 2, 10, 10)
        self.warning_label = dict()
        self.text_ctrl = dict()

        for col in column_list:
            self.warning_label[col] = CenterText(self)
            self.warning_label[col].SetForegroundColour(wx.RED)

            self.text_ctrl[col] = wx.TextCtrl(self,
                                              style=wx.ALIGN_CENTER_VERTICAL)

            input_sizer.AddStretchSpacer(1)
            input_sizer.AddMany([(self.warning_label[col], 1, wx.EXPAND),
                                 (CenterText(self, source[col]), 1, wx.EXPAND),
                                 (self.text_ctrl[col], 1, wx.EXPAND)])

        input_sizer.AddGrowableCol(0, 1)
        input_sizer.AddGrowableCol(1, 2)

        outer_sizer = wx.BoxSizer(wx.VERTICAL)
        outer_sizer.Add(input_sizer, 0, wx.ALL | wx.EXPAND, border=5)
        outer_sizer.Add(self._get_buttons(), 0, wx.ALL | wx.EXPAND, border=5)
        self.SetSizerAndFit(outer_sizer)

        self.SetSize(320, -1)
        self.Center()

    def _get_buttons(self):
        ok_btn = wx.Button(self, label=locale.OK)
        cancel_btn = wx.Button(self, label=locale.CANCEL)

        sizer = wx.GridSizer(1, 2, 0, 10)

        sizer.Add(ok_btn, 1, wx.EXPAND)
        sizer.Add(cancel_btn, 1, wx.EXPAND)

        ok_btn.Bind(wx.EVT_BUTTON, self._on_ok)
        cancel_btn.Bind(wx.EVT_BUTTON, self._on_cancel)

        return sizer

    def _on_ok(self, e):
        pass

    def _on_cancel(self, e):
        pass
