import wx
import ObjectListView as Olv

import model
from .dbview import DbView
from .customerdialog import CustomerDial
from model.db_description import order
from .locale import rus as locale


class CustomerTab(wx.Panel):
    def __init__(self, parent):
        super(CustomerTab, self).__init__(parent)

        self.column_sizer = wx.BoxSizer(wx.VERTICAL)

        self.customer_text = wx.StaticText(self)
        self.column_sizer.Add(self.customer_text, 0, wx.BOTTOM | wx.EXPAND,
                              border=10)
        self.customer_text.SetLabelText(locale.CUSTOMER_NOT_CHOSEN)

        self._get_buttons()

        self.db_list = DbView(self, order)
        self.db_list.CreateCheckStateColumn()

        self.outer_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.outer_sizer.Add(self.db_list, 1, wx.EXPAND)
        self.outer_sizer.AddSpacer(4)
        self.outer_sizer.Add(self.column_sizer, 0, wx.EXPAND)

        self.SetSizer(self.outer_sizer)

        self.shop = model.Shop()
        self.shop.ui_set_order = self.set_order

    def _get_buttons(self):
        self.customer_btn = wx.Button(self, label=locale.CHOOSE_CUSTOMER_BTN)
        place_order_btn = wx.Button(self, label=locale.PLACE_ORDER_BTN)
        clear_order_btn = wx.Button(self, label=locale.CLEAR_ORDER_BTN)

        self.column_sizer.Add(self.customer_btn, 0, wx.EXPAND)

        self.column_sizer.AddSpacer(50)

        self.column_sizer.Add(place_order_btn, 0, wx.BOTTOM | wx.EXPAND,
                              border=10)
        self.column_sizer.Add(clear_order_btn, 0, wx.EXPAND)

        self.Bind(wx.EVT_BUTTON, self._on_change_customer, self.customer_btn)
        self.Bind(wx.EVT_BUTTON, self._on_place_order, place_order_btn)
        self.Bind(wx.EVT_BUTTON, self._on_clear_order, clear_order_btn)

    def _on_change_customer(self, e):
        with CustomerDial(self) as dlg:
            if dlg.ShowModal() == wx.OK:
                pass

    def _on_place_order(self, e):
        pass

    def _on_clear_order(self, e):
        pass

    def set_order(self):
        self.shop.ui_set_products()
        self.db_list.SetObjects(self.shop.get_order())
        self._display_customer()

    def _display_customer(self):
        pass
