import wx

import ObjectListView as Olv


class DbView(Olv.ObjectListView):
    def __init__(self, parent, table_name):
        super(DbView, self).__init__(parent, style=wx.LC_REPORT)

        for column in table_name.columns:
            new_col = Olv.ColumnDefn(column.display_name, isSpaceFilling=True,
                                     valueGetter=column.name,
                                     minimumWidth=column.proportion * 40)
            new_col.freeSpaceProportion = column.proportion
            self.AddColumnDefn(new_col)
