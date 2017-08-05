import wx

APP_NAME = 'Shop UI'


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MainWindow, self).__init__(parent, title=title)

        self.init_ui()

    def init_ui(self):
        help_menu = wx.Menu()
        about_item = help_menu.Append(wx.ID_ABOUT, "About {}".format(APP_NAME))

        menu_bar = wx.MenuBar()
        menu_bar.Append(help_menu, "Help")
        self.SetMenuBar(menu_bar)

        self.Bind(wx.EVT_MENU, self.on_about, about_item)

        self.SetSize((900, 500))  # TODO: make constant
        self.Show(True)

    def on_about(self, event):
        dlg = wx.MessageDialog(self, "About {}".format(APP_NAME), APP_NAME)
        dlg.ShowModal()
        dlg.Destroy()


app = wx.App(False)
MainWindow(None, APP_NAME)
app.MainLoop()
