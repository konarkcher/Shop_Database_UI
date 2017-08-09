import wx

from model.db_description import storage
from .dbview import DbView
from .locale import rus as locale


class ShopTab(wx.Panel):
    def __init__(self, parent):
        super(ShopTab, self).__init__(parent)

        button_sizer = self._get_buttons()

        self.db_list = DbView(self, storage['products'])

        outer_sizer = wx.BoxSizer(wx.HORIZONTAL)

        outer_sizer.Add(self.db_list, 1, wx.EXPAND)
        outer_sizer.AddSpacer(4)
        outer_sizer.Add(button_sizer, 0, wx.TOP)

        self.SetSizer(outer_sizer)

    def _get_buttons(self):
        button_sizer = wx.GridSizer(4, 1, 10, 0)  # rows, cols, vgap, hgap

        buttons = [wx.Button(self, label=locale.ADD_BUTTON),
                   wx.Button(self, label=locale.DELETE_BUTTON),
                   wx.Button(self, label=locale.TO_CART_BUTTON)]
        for button in buttons:
            button_sizer.Add(button, 1, wx.EXPAND)

        for func, button in zip([self._on_add, self._on_delete,
                                 self._on_to_cart], buttons):
            self.Bind(wx.EVT_BUTTON, func, button)

        return button_sizer

    def _on_add(self, e):
        print('on add')

    def _on_delete(self, e):
        print('on delete')

    def _on_to_cart(self, e):
        print('on to cart')
