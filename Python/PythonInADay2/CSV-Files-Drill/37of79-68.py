
import wx

class Frame(wx.Frame):
    # Added title parameter
    def __init__(self, title):
        # title = title variable
        wx.Frame.__init__(self, None,\
          title=title, size=(300,200))

app = wx.App()
# Pass in the frame title
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()
