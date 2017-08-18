import wx

import db.exception as ex
from .locale import rus as locale


def error_message(e):
    wx.MessageBox(locale.DE[e.type_num], locale.ERROR)
