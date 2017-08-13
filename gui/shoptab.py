import wx

from .dbpanel import DbPanel
import model
from model.db_description import storage
from .locale import rus as locale


class ShopTab(DbPanel):
    def __init__(self, parent):
        super(ShopTab, self).__init__(parent, storage['products'],
                                      locale.ADD_PRODUCT)

        self.db_list.CreateCheckStateColumn()
        self.shop = model.Shop()

        self.button_sizer.AddSpacer(50)
        to_cart_btn = wx.Button(self, label=locale.TO_CART_BUTTON)
        self.button_sizer.Add(to_cart_btn, 0, wx.EXPAND)

        self.Bind(wx.EVT_BUTTON, self._on_to_cart, to_cart_btn)
        self.shop.ui_set_products = self.set_data

    def set_data(self):
        data = [model.Product(x) for x in self.shop.get_from('products')]
        self.db_list.SetObjects(data)

    def _on_delete(self, e):
        kill_list = self.db_list.GetCheckedObjects()
        self.shop.delete_from('products', [x.id for x in kill_list])
        self.db_list.RemoveObjects(kill_list)

    def _on_to_cart(self):
        pass
