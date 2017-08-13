import wx

import model
from .dbpanel import DbPanel
from model.db_description import storage
from .locale import rus as locale


class CustomerDial(wx.Dialog):
    def __init__(self, parent):
        super(CustomerDial, self).__init__(parent)

        self._customer_id = None

        self.shop = model.Shop()
        panel = DbPanel(self, storage['customers'], locale.ADD_CUSTOMER)

        choose_btn = wx.Button(panel, label=locale.CHOOSE)
        cancel_btn = wx.Button(panel, label=locale.CANCEL)

        panel.button_sizer.AddSpacer(50)
        panel.button_sizer.Add(choose_btn, 0, wx.BOTTOM | wx.EXPAND, border=10)
        panel.button_sizer.Add(cancel_btn, 0, wx.EXPAND)

        self.Bind(wx.EVT_BUTTON, self._on_choose, choose_btn)
        self.Bind(wx.EVT_BUTTON, self._on_cancel, cancel_btn)

        panel.db_list.SetObjects([model.Customer(x) for x in
                                  self.shop.get_from('customers')])
        print(list(self.shop.get_from('customers')))

        self.SetSize((900, 300))
        self.SetTitle(locale.CHOOSE_CUSTOMER_TITLE)

    def _on_choose(self, e):
        self.EndModal(wx.OK)

    def _on_cancel(self, e):
        self.EndModal(wx.CANCEL)

    def get_id(self):
        return self._customer_id
