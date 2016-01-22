import wx
import db_program


class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None,\
          title=title, size=(800,700))
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
        # Create static box
        wx.StaticBox(panel, label='Create a new HTML page', pos=(20,40), size=(280,190))
        
        # Text for name, gender etc
        wx.StaticText(panel, label='Title:', pos=(30,70))
        wx.StaticText(panel, label='Body:', pos=(30,110))
        wx.StaticText(panel, label='Paragraph:', pos=(30,150))
        wx.StaticText(panel, label='Footer:', pos=(30,190))
        
        # Single line text boxes
        self.sTitle = wx.TextCtrl(panel, size=(150, -1), pos=(130,70))
        self.sBody = wx.TextCtrl(panel, size=(150, -1), pos=(130,110))
        self.sParagraph = wx.TextCtrl(panel, size=(150, -1), pos=(130, 150))
        self.sFooter = wx.TextCtrl(panel, size=(150, -1), pos=(130,190))
        
        # Save button
        save = wx.Button(panel, label="Create HTML", pos=(100, 230))
        save.Bind(wx.EVT_BUTTON, self.addCharacter)
        
        # Setup the Table UI
        # Setup table as listCtrl
        self.listCtrl = wx.ListCtrl(panel, size=(400,400), pos=(350,40), style=wx.LC_REPORT |wx.BORDER_SUNKEN)
        
        # Add columns to listCtrl
        self.listCtrl.InsertColumn(0, "ID")
        self.listCtrl.InsertColumn(1, "Title")
        self.listCtrl.InsertColumn(2, "Body")
        self.listCtrl.InsertColumn(3, "Paragraph")
        self.listCtrl.InsertColumn(4, "Footer")
        
        # Add data to the list control
        self.fillListCtrl()
        
        # Run onSelect function when item is selected
        self.listCtrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelect)
        
        # Setup a delete button
        deleteBtn = wx.Button(panel, label="Delete", pos=(520, 450))
        
        # Bind delete button to onDelete function
        deleteBtn.Bind(wx.EVT_BUTTON, self.onDelete)

          
        # Setup Update Character UI
        # Create static box
        wx.StaticBox(panel, label='Update the HTML', pos=(20,340), size=(280,190))
        
        # Text for name, gender etc
        wx.StaticText(panel, label='Title:', pos=(30,370))
        wx.StaticText(panel, label='Body', pos=(30,410))
        wx.StaticText(panel, label='Paragraph:', pos=(30,450))
        wx.StaticText(panel, label='Footer:', pos=(30,490))
        
        # Single line text boxes
        self.sTitleU = wx.TextCtrl(panel, size=(150, -1), pos=(130,370))
        self.sBodyU = wx.TextCtrl(panel, size=(150, -1), pos=(130,410))
        self.sParagraphU = wx.TextCtrl(panel, size=(150, -1), pos=(130, 450))
        self.sFooterU = wx.TextCtrl(panel, size=(150, -1), pos=(130,490))
        
        # Save button
        saveUpdate = wx.Button(panel, label="Update HTML", pos=(50, 530))
        saveUpdate.Bind(wx.EVT_BUTTON, self.updateHTML)

        # Setup a view HTML button
        viewBtn = wx.Button(panel, label="View HTML", pos=(200, 530))
        viewBtn.Bind(wx.EVT_BUTTON, self.onView)
        
    def addCharacter(self, event):
        title = self.sTitle.GetValue()
        body = self.sBody.GetValue()
        paragraph = self.sParagraph.GetValue()
        footer = self.sFooter.GetValue()
        
        # Checking if variables have a value
        if (title == '') or (body == '') or (paragraph == '') or (footer == ''):
            # Alert user that a variable is empty
            dlg = wx.MessageDialog(None, \
                'Some HTML details are missing. Enter values in each text box.', \
                'Missing Details', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            
            return False
        
        # Adding character to database
        db_program.newHTML(title, body, paragraph, footer)
        print db_program.viewAll()
        
        # Empty text boxes when finished.
        self.sTitle.Clear()
        self.sBody.Clear()
        self.sParagraph.Clear()
        self.sFooter.Clear()
        
        # Update list control
        self.fillListCtrl()
    
    def exitProgram(self, event):
        self.Destroy()
        
    def fillListCtrl(self):        
        # Get data from the database
        self.allData = db_program.viewAll()
        
        # Delete old data before adding new data
        self.listCtrl.DeleteAllItems()
        
        # Append data to the table
        for row in self.allData:
            # Loop though and append data
            self.listCtrl.Append(row)
            
    def onDelete(self, event):
        # Delete the character
        db_program.deleteHTML(self.selectedId)
        
        # Refresh the table
        self.fillListCtrl()

        # Empty text boxes when finished.
        self.sTitleU.Clear()
        self.sBodyU.Clear()
        self.sParagraphU.Clear()
        self.sFooterU.Clear()

    def onSelect(self, event):
        # Get the id of the selected row
        self.selectedId = event.GetText()
        
        # Get index of selected row
        index = event.GetIndex()
        
        # Get character info
        charInfo = self.allData[index]
        print charInfo
        
        # Set value of update text boxes
        self.sTitleU.SetValue(charInfo[1])
        self.sBodyU.SetValue(charInfo[2])
        self.sParagraphU.SetValue(charInfo[3])
        self.sFooterU.SetValue(charInfo[4])
    
    def updateHTML(self, event):
        # Get the updated values
        title = self.sTitleU.GetValue()
        body = self.sBodyU.GetValue()
        paragraph = self.sParagraphU.GetValue()
        footer = self.sFooterU.GetValue()
        
        # Get character ID
        htmlId = self.selectedId
        
        # Update the character
        db_program.updateHTML(htmlId, title, body, paragraph, footer)
        
        # Refresh list control
        self.fillListCtrl()

    def onView(self, event):

        import webbrowser
        f = open('stayTuned.html','w')

        titleText = self.sTitleU.GetValue()
        bodyText = self.sBodyU.GetValue()
        paragraphText = self.sParagraphU.GetValue()
        footerText = self.sFooterU.GetValue()

        wrapper = """
        <!DOCTYPE html>
        <html>
        <head>
        <title>
        %s
        </title>
        </head>
        <body>
        <h1>
        %s
        </h1>
        <p>
        <h3>
        %s
        </h3>
        </p>
        <footer>
        <p><h6>
        %s
        </h6>
        </p>
        </footer>
        </body>
        </html>
        """

        message = wrapper % (titleText, bodyText, paragraphText, footerText)

        f.write(message),(titleText, bodyText, paragraphText, footerText)
        f.close()

        webbrowser.open_new_tab('stayTuned.html')
    
app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()
