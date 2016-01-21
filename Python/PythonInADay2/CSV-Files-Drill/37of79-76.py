import wx

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None,\
          title=title, size=(300,200))
        panel = wx.Panel(self)
        button = wx.Button(panel,label="Exit",size=(100,40),pos=(100,30))
        # Bind button event to the function self.exit
        button.Bind(wx.EVT_BUTTON, self.exit)
        
        # Create menu bar
        menuBar = wx.MenuBar()
        # Create wx menus
        fileMenu = wx.Menu()
        editMenu = wx.Menu()
        
        # Add items to fileMenu
        fileMenu.Append(wx.NewId(), "New File")
        fileMenu.Append(wx.NewId(), "Open")
        fileMenu.Append(wx.NewId(), "Exit")
        
        # Add fileMenu and editMenu to menuBar
        menuBar.Append(fileMenu, "File")
        menuBar.Append(editMenu, "Edit")
        
        self.SetMenuBar(menuBar)
    
    def exit(self, event):
        self.Destroy()

app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()
