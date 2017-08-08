import wx

from .dialogans import DlgAnswer
from .locale import rus as locale


class SqliteTab(wx.Panel):
    def __init__(self, parent):
        super(SqliteTab, self).__init__(parent)

        self._res = DlgAnswer.NOT_CHOSEN

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(wx.StaticText(self, label=locale.FILE), 0, wx.LEFT, border=1)

        self.path_text = wx.StaticText(self)
        sizer.Add(self.path_text, 1)

        open_btn = wx.Button(self, label='...', size=(30, -1))
        create_btn = wx.Button(self, label='+', size=(30, -1))
        for btn in [open_btn, create_btn]:
            sizer.Add(btn, 0, wx.LEFT | wx.TOP, border=1)

        self.SetSizer(sizer)

        self.Bind(wx.EVT_BUTTON, self._on_open, open_btn)
        self.Bind(wx.EVT_BUTTON, self._on_create, create_btn)

    def _on_open(self, e):
        with wx.FileDialog(self, '',
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as dlg:
            if dlg.ShowModal() != wx.ID_CANCEL:
                self._res = DlgAnswer.SQLITE_OPEN
                self.path_text.SetLabelText(dlg.GetPath())

    def _on_create(self, e):
        with wx.FileDialog(self, '', style=wx.FD_SAVE) as dlg:
            if dlg.ShowModal() != wx.ID_CANCEL:
                self._res = DlgAnswer.SQLITE_CREATE
                self.path_text.SetLabelText(dlg.GetPath())

    def get_res(self):
        return self._res, self.path_text.GetLabelText()


class DbSetDial(wx.Dialog):
    def __init__(self, parent):
        super(DbSetDial, self).__init__(parent)

        self._res = DlgAnswer.NOT_CHOSEN
        self._data = None

        panel = wx.Panel(self)

        self.notebook = wx.Notebook(panel)
        self.sqlitetab = SqliteTab(self.notebook)
        self.notebook.AddPage(self.sqlitetab, locale.SQLITE_DB)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.notebook, 1, wx.EXPAND)

        bottom_sizer = wx.GridSizer(1, 2, 2, 0)  # rows, cols, vgap, hgap

        accept_btn = wx.Button(panel, label=locale.ACCEPT)
        cancel_btn = wx.Button(panel, label=locale.CANCEL)
        for btn in [accept_btn, cancel_btn]:
            bottom_sizer.Add(btn, 1, wx.BOTTOM | wx.EXPAND)

        sizer.Add(bottom_sizer, 0, wx.BOTTOM | wx.LEFT | wx.RIGHT | wx.EXPAND,
                  border=6)

        panel.SetSizer(sizer)

        self.Bind(wx.EVT_BUTTON, self._on_accept, accept_btn)
        self.Bind(wx.EVT_BUTTON, self._on_cancel, cancel_btn)

        self.SetSize((400, 200))
        self.SetTitle(locale.SET_DB)

    def _on_accept(self, e):
        self._res, self._data = self.notebook.GetCurrentPage().get_res()

        if self._res is DlgAnswer.NOT_CHOSEN:
            return

        self.EndModal(wx.OK)

    def _on_cancel(self, e):
        self.EndModal(wx.CANCEL)

    def get_res(self):
        return self._res, self._data
