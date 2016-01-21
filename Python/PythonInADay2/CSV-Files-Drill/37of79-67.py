
import wx

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Python GUI", size=(300,200))

app = wx.App()
frame = Frame()
frame.Show()
app.MainLoop()
