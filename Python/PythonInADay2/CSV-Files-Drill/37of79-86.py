import wx

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None,\
          title=title, size=(300,250))
        panel = wx.Panel(self)
        
        wx.TextCtrl(panel, size=(200, -1), pos=(50,30))
        wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(200, 100), pos=(50,80))

app = wx.App()
frame = Frame("wxPython Widgets!")
frame.Show()
app.MainLoop()
