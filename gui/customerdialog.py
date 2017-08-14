import wx

import model
from .dbpanel import DbPanel
from model.db_description import storage
from .locale import rus as locale


class CustomerTab(DbPanel):
    def __init__(self, parent):
        super(CustomerTab, self).__init__(parent, storage['customers'],
                                          locale.ADD_CUSTOMER)

        self.shop = model.Shop()

        self.choose_btn = wx.Button(self, label=locale.CHOOSE)
        self.cancel_btn = wx.Button(self, label=locale.CANCEL)

        self.button_sizer.AddSpacer(50)
        self.button_sizer.Add(self.choose_btn, 0, wx.BOTTOM | wx.EXPAND,
                              border=10)
        self.button_sizer.Add(self.cancel_btn, 0, wx.EXPAND)

        self.db_list.SetObjects([model.Customer(x) for x in
                                 self.shop.get_from('customers')])

    def _on_delete(self, e):
        select = self.db_list.GetSelectedObject()
        if select is None:
            return

        self.shop.delete_from('customers', [select.id])
        self.db_list.RemoveObject(select)


class CustomerDial(wx.Dialog):
    def __init__(self, parent):
        super(CustomerDial, self).__init__(parent)

        self._customer = None

        self.panel = CustomerTab(self)
        self.panel.db_list.SetEmptyListMsg(locale.CUSTOMER_LC)

        self.Bind(wx.EVT_BUTTON, self._on_choose, self.panel.choose_btn)
        self.Bind(wx.EVT_BUTTON, self._on_cancel, self.panel.cancel_btn)

        self.SetSize((900, 300))
        self.SetTitle(locale.CHOOSE_CUSTOMER_TITLE)

    def _on_choose(self, e):
        selected = self.panel.db_list.GetSelectedObject()
        if selected is None:
            return

        self._customer = selected
        self.EndModal(wx.OK)

    def _on_cancel(self, e):
        self.EndModal(wx.CANCEL)

    def get_customer(self):
        return self._customer
