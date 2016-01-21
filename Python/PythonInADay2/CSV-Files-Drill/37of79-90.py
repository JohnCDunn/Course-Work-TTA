import wx

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None,\
          title=title, size=(800,600))
        panel = wx.Panel(self)
    
        # Creating the menu bar
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.NewId(), "Exit")
        menuBar.Append(fileMenu, "File")
        
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.exitProgram, exitItem)
        
        self.CreateStatusBar()
            
    def exitProgram(self, event):
        self.Destroy()
    
app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()
