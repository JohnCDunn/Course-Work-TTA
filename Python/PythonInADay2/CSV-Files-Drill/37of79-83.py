import wx

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None,\
          title=title, size=(300,250))
        panel = wx.Panel(self)
        
        simpsons = ['Bart', 'Lisa', 'Maggie', 'Marge', 'Homer']
        cb = wx.ComboBox(panel, pos=(100, 50), choices=simpsons, style=wx.CB_READONLY)

app = wx.App()
frame = Frame("wxPython Widgets!")
frame.Show()
app.MainLoop()
