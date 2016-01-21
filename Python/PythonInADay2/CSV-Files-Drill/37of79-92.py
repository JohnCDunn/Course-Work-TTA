import wx, db_program

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
        
        # Setup Add New Character UI
        # Text at the top
        wx.StaticText(panel, label='Add a new character', pos=(30,40))
        
        # Text for name, gender etc
        wx.StaticText(panel, label='Name:', pos=(30,70))
        wx.StaticText(panel, label='Gender:', pos=(30,110))
        wx.StaticText(panel, label='Age:', pos=(30,150))
        wx.StaticText(panel, label='Occupation:', pos=(30,190))
        
        # Single line text boxes
        wx.TextCtrl(panel, size=(150, -1), pos=(130,70))
        wx.TextCtrl(panel, size=(150, -1), pos=(130,110))
        wx.TextCtrl(panel, size=(150, -1), pos=(130,150))
        wx.TextCtrl(panel, size=(150, -1), pos=(130,190))
        
    def exitProgram(self, event):
        self.Destroy()
    
app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()
