import wx

import ObjectListView as Olv

import db
import db.adapter
from .locale import rus as locale


class DbOlv(Olv.ObjectListView):
    def __init__(self, parent):
        super(DbOlv, self).__init__(parent, style=wx.LC_REPORT)

        for (index, name), prop in zip(enumerate(locale.COL), [1, 5, 2, 2, 2]):
            new_col = Olv.ColumnDefn(name, isSpaceFilling=True,
                                     valueGetter=index, minimumWidth=prop * 40)
            new_col.freeSpaceProportion = prop
            self.AddColumnDefn(new_col)

        self.CreateCheckStateColumn()

        self.SetEmptyListMsg('No items or db is not connected')


class ShopTab(wx.Panel):
    def __init__(self, parent):
        super(ShopTab, self).__init__(parent)

        button_sizer = self._get_buttons()

        self.db_list = DbOlv(self)

        outer_sizer = wx.BoxSizer(wx.HORIZONTAL)

        outer_sizer.Add(self.db_list, 1, wx.EXPAND)
        outer_sizer.AddSpacer(4)
        outer_sizer.Add(button_sizer, 0, wx.TOP)

        self.SetSizer(outer_sizer)

        self.database = db.DbManager(db.adapter.Sqlite3('./data/shop'))
        self._set_db_data()

        self.Bind(wx.EVT_WINDOW_DESTROY, self._on_destroy, self)

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

    def _set_db_data(self):
        self.db_list.SetObjects(list(self.database.select_all('storage')))

    def _on_add(self, e):
        print('on add')

    def _on_delete(self, e):
        print('on delete')

    def _on_to_cart(self, e):
        print('on to cart')

    def _on_destroy(self, event):
        self.database.close_connection()
