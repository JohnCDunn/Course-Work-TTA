#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
ZetCode wxPython tutorial

This example shows a simple menu.

author: Jan Bodnar
website: www.zetcode.com
last modified: September 2011
'''

import wx

class Example(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs) 
            
        self.InitUI()

             
        self.button1 = wx.Button(self, id=-1, label='Button1',
            pos=(8, 8), size=(175, 28))
        self.button1.Bind(wx.EVT_BUTTON, self.button1Click)
        
        self.button2 = wx.Button(self, id=-1, label='Button2',
            pos=(8, 38), size=(175, 28))
        self.button2.Bind(wx.EVT_BUTTON, self.button2Click)
       
        
    def InitUI(self):    

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)

        self.SetSize((300, 200))
        self.SetTitle('Simple menu')
        self.Centre()
        self.Show(True)
        
    def OnQuit(self, e):
        self.Close()

    def button1Click(self,event):
        self.button1.Disable()
        self.SetTitle("Button1 clicked")
        self.button2.Enable()

    def button2Click(self,event):
        self.button2.Disable()
        self.SetTitle("Button2 clicked")
        self.button1.Enable()

def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()
