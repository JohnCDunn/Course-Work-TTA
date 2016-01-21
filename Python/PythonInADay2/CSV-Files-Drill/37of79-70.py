import wx

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None,\
          title=title, size=(300,200))
        panel = wx.Panel(self)
        button = wx.Button(panel,label="Exit",size=(100,40),pos=(100,30))

app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()
