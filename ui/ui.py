import wx
import rus_locale as locale

APP_NAME = 'Shop UI'


class ShopTab(wx.Panel):
    def __init__(self, parent):
        super(ShopTab, self).__init__(parent)


class CustomerTab(wx.Panel):
    def __init__(self, parent):
        super(CustomerTab, self).__init__(parent)


class ShopNotebook(wx.Notebook):
    def __init__(self, parent):
        super(ShopNotebook, self).__init__(parent)

        self.AddPage(ShopTab(self), locale.shop_tab)
        self.AddPage(CustomerTab(self), locale.customer_tab)


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MainWindow, self).__init__(parent, title=title)

        self.init_menubar()
        self.init_toolbar()

        panel = wx.Panel(self)
        notebook = ShopNotebook(panel)

        sizer = wx.BoxSizer()
        sizer.Add(notebook, 1, wx.EXPAND)
        panel.SetSizer(sizer)

        self.SetSize((900, 500))  # TODO: make constant
        self.Show(True)

    def init_menubar(self):
        menu_bar = wx.MenuBar()

        # file_menu = wx.Menu() # TODO: add compatibility for non-mac
        # quit_item = file_menu.Append(wx.ID_CLOSE, "Quit {}".format(APP_NAME))
        # menu_bar.Append(file_menu, "File")

        help_menu = wx.Menu()
        about_item = help_menu.Append(wx.ID_ABOUT, "About {}".format(APP_NAME))
        menu_bar.Append(help_menu, "Help")

        self.SetMenuBar(menu_bar)

        self.Bind(wx.EVT_MENU, self.on_about, about_item)

    def init_toolbar(self):
        toolbar = self.CreateToolBar(style=wx.RIGHT)
        set_tool = toolbar.AddTool(wx.ID_ANY, 'Settings', wx.Bitmap('set.png'))
        toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.on_set, set_tool)

    def on_about(self, event):
        dlg = wx.MessageDialog(self, "About {}".format(APP_NAME), APP_NAME)
        dlg.ShowModal()
        dlg.Destroy()

    def on_set(self, event):
        pass


app = wx.App(False)
MainWindow(None, APP_NAME)
app.MainLoop()
