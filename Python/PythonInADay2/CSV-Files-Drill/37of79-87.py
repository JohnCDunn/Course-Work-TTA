import wx

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None,\
          title=title, size=(300,250))
        panel = wx.Panel(self)
        
        wx.SpinCtrl(panel, value='0', pos=(130, 50), size=(70, 25))


app = wx.App()
frame = Frame("wxPython Widgets!")
frame.Show()
app.MainLoop()
