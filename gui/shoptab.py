import wx
import ObjectListView as Olv

import model
from db import exception as ex
from .error_message import error_message
from .dbpanel import DbPanel
from .adddialog import AddDialog
from model.db_description import storage
from .locale import rus as locale


class ShopTab(DbPanel):
    def __init__(self, parent):
        super(ShopTab, self).__init__(parent, storage['products'],
                                      locale.ADD_PRODUCT)

        self.db_list.InstallCheckStateColumn(self.db_list.columns[0])
        self.db_list.SetEmptyListMsg(locale.PRODUCT_LC)

        self.db_list.cellEditMode = self.db_list.CELLEDIT_DOUBLECLICK
        for i in range(1, 4):
            self.db_list.columns[i].isEditable = True

        self.db_list.Bind(Olv.EVT_CELL_EDIT_STARTING, self._reserve_checker)
        self.db_list.Bind(Olv.EVT_CELL_EDIT_FINISHING, self._update_checker)

        self.shop = model.Shop()

        self.button_sizer.AddSpacer(50)
        to_cart_btn = wx.Button(self, label=locale.TO_CART_BUTTON)
        self.button_sizer.Add(to_cart_btn, 0, wx.EXPAND)

        self.Bind(wx.EVT_BUTTON, self._on_to_cart, to_cart_btn)
        self.shop.ui_display_products = self._display_data

    def _reserve_checker(self, e):
        if e.rowModel.reserved > 0:
            error_message(message=locale.UPDATE_RESERVED)
            e.Veto()

    def _update_checker(self, evt):
        col_name = evt.objectListView.columns[evt.subItemIndex].valueGetter
        upd_id = evt.rowModel.id
        value = evt.editor.Value

        try:
            self.shop.update('products', col_name, upd_id, value)
        except ex.DbException as e:
            error_message(e)
            evt.Veto()
        except ex.ConstraintException as e:
            error_message(message=locale.CE[e.type_num])
            evt.Veto()

    def _display_data(self):
        data = [model.Product(x) for x in self.shop.get_from('products')]
        self.db_list.SetObjects(data)

    def _on_delete(self, e):
        kill_list = self.db_list.GetCheckedObjects()

        try:
            self.shop.delete_from('products', [x.id for x in kill_list])
        except ex.DbException as e:
            error_message(e)

        self.db_list.RemoveObjects(kill_list)

    def _on_to_cart(self, e):
        selected = self.db_list.GetCheckedObjects()
        if [x for x in selected if x.count <= x.reserved]:
            wx.MessageBox(locale.LACK, locale.ERROR)
            return

        try:
            self.shop.to_cart(selected)
        except ex.DbException as e:
            error_message(e)

    def _on_add(self, e):
        with AddDialog(self, locale.NEW_PRODUCT, storage['products'],
                       self.shop.add_product) as dlg:
            if dlg.ShowModal() == wx.OK:
                self._display_data()
