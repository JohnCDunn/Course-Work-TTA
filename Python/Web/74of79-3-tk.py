#!/usr/bin/python3
# feedback_solution.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com
import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
import db_program


class HTMLBuild():

    def __init__(self, master):
        
        master.title('Build A HTML Page')
        #master.resizable(False, False)

        self.style = ttk.Style()



        #Input frame
        self.frame_input = ttk.LabelFrame(master, text="Create New HTML Page")
        self.frame_input.grid(row=0, column = 0, sticky='nw', pady=40)

        ttk.Label(self.frame_input, text = 'Title:').grid(row = 0, column = 0, padx = 5, pady=8,sticky = 'sw')
        ttk.Label(self.frame_input, text = 'Body:').grid(row = 1, column = 0, padx = 5, pady=8,sticky = 'sw')
        ttk.Label(self.frame_input, text = 'Paragraph:').grid(row = 2, column = 0, padx = 5, pady=8,sticky = 'sw')
        ttk.Label(self.frame_input, text = 'Footer:').grid(row = 3, column = 0, padx = 5, pady=8,sticky = 'sw')

        self.entry_title = ttk.Entry(self.frame_input, width = 24, font = ('Arial', 10))
        self.entry_body = ttk.Entry(self.frame_input, width = 24, font = ('Arial', 10))
        self.entry_paragraph = ttk.Entry(self.frame_input, width = 24, font = ('Arial', 10))
        self.entry_footer = ttk.Entry(self.frame_input, width = 24, font = ('Arial', 10))

        self.entry_title.grid(row = 0, column = 2, padx = 5, pady=8)
        self.entry_body.grid(row = 1, column = 2,pady=8, padx = 5)
        self.entry_paragraph.grid(row = 2, column = 2, pady=8,padx = 5)
        self.entry_footer.grid(row = 3, column = 2, pady=8,padx = 5)

        ttk.Button(self.frame_input, text = 'Create HTML',
                   command = self.submit).grid(row = 4, column = 0, columnspan=2, padx = 5, pady = 5, sticky = 'w')

        #Update frame
        self.frame_update = ttk.LabelFrame(master, text="Update HTML Page")
        self.frame_update.grid(row=1, column = 0, sticky='nw', pady=40)

        ttk.Label(self.frame_update, text = 'Title:').grid(row = 0, column = 0, padx = 5, pady=8, sticky = 'sw')
        ttk.Label(self.frame_update, text = 'Body:').grid(row = 1, column = 0, padx = 5, pady=8, sticky = 'sw')
        ttk.Label(self.frame_update, text = 'Paragraph:').grid(row = 2, column = 0, padx = 5, pady=8, sticky = 'sw')
        ttk.Label(self.frame_update, text = 'Footer:').grid(row = 3, column = 0, padx = 5, pady=8, sticky = 'sw')


        self.update_title = ttk.Entry(self.frame_update, width = 24, font = ('Arial', 10))
        self.update_body = ttk.Entry(self.frame_update, width = 24, font = ('Arial', 10))
        self.update_paragraph = ttk.Entry(self.frame_update, width = 24, font = ('Arial', 10))
        self.update_footer = ttk.Entry(self.frame_update, width = 24, font = ('Arial', 10))

        self.update_title.grid(row = 0, column = 1, padx = 5)
        self.update_body.grid(row = 1, column = 1, padx = 5)
        self.update_paragraph.grid(row = 2, column = 1, padx = 5)
        self.update_footer.grid(row = 3, column = 1, padx = 5)

        ttk.Button(self.frame_update, text = 'Update HTML',
                   command = self.updateHTML).grid(row = 4, column = 0, padx = 5, pady = 5)
        ttk.Button(self.frame_update, text = 'View HTML',
                   command = self.viewHTML).grid(row = 4, column = 1, padx = 5, pady = 5)


        #HTML List frame
        self.frame_list_html = ttk.LabelFrame(master, text="List HTML Pages")
        self.frame_list_html.grid(row=0, column = 1, rowspan=4, sticky='ne', padx = 20, pady=40)


        self.htmlTree = ttk.Treeview(columns=html_header, show="headings")
        # create a treeview with dual scrollbars
        self.htmlTree = ttk.Treeview(columns=html_header, show="headings")
        vsb = ttk.Scrollbar(orient="vertical",
            command=self.htmlTree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",
            command=self.htmlTree.xview)
        self.htmlTree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.htmlTree.grid(column=3, row=0, sticky='nsew', in_=self.frame_list_html)
        vsb.grid(column=4, row=0, sticky='ns', in_=self.frame_list_html)
        hsb.grid(column=3, row=1, sticky='ew', in_=self.frame_list_html)
        self.frame_list_html.grid_columnconfigure(3, weight=1)
        self.frame_list_html.grid_rowconfigure(3, weight=1)

        for col in html_header:
            self.htmlTree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.htmlTree, c, 0))
            # adjust the column's width to the header string
            self.htmlTree.column(col,
                width=tkFont.Font().measure(col.title()))

        # Get data from the database
        html_list= db_program.viewAll()
        print (html_list)

        for item in html_list:
            print (item)
            
            self.htmlTree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.htmlTree.column(html_header[ix],width=None)<col_w:
                    self.htmlTree.column(html_header[ix], width=col_w)

        self.htmlTree.bind("<ButtonRelease-1>", self.selection)

        ttk.Button(self.frame_list_html, text = 'Delete',
                   command = self.onDelete).grid(row = 5, column = 0, columnspan=4, padx = 5, pady = 8)




    def submit(self):
        title = self.entry_title.get()
        body = self.entry_body.get()
        paragraph = self.entry_paragraph.get()
        footer = self.entry_footer.get()

        # Adding character to database
        db_program.newHTML(title, body, paragraph, footer)

        # Empty text boxes when finished.
        self.entry_title.delete(0, END)
        self.entry_body.delete(0, END)
        self.entry_paragraph.delete(0, END)
        self.entry_footer.delete(0, END)

        # Update tree view
        self.updateTreeView()
        messagebox.showinfo(title = 'Process HTML', message = 'HTML Submitted!')

    def updateHTML(self):
        # Get the updated values
        print ("update HTML")
        title = self.update_title.get()
        body = self.update_body.get()
        paragraph = self.update_paragraph.get()
        footer = self.update_footer.get()

        #get html ID
        ID = self.selectedId

        print ("ID + " + str(ID))

        # Update the HTML
        db_program.updateHTML(ID, title, body, paragraph, footer)

        # Refresh list control
        self.updateTreeView()
        messagebox.showinfo(title = 'Process HTML', message = 'HTML Updated!')


    def viewHTML(self):

        import webbrowser
        f = open('viewHtml.html','w')

        titleText = self.update_title.get()
        bodyText = self.update_body.get()
        paragraphText = self.update_paragraph.get()
        footerText = self.update_footer.get()

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

        webbrowser.open_new_tab('viewHtml.html')


    def selection(self, event):

        #Clean out the update text boxes
        self.update_title.delete(0, END)
        self.update_body.delete(0, END)
        self.update_paragraph.delete(0, END)
        self.update_footer.delete(0, END)

        curItem = self.htmlTree.focus()
        #print (self.htmlTree.item(curItem))
        curString = self.htmlTree.item(curItem)

        curValues = curString.pop('values')

        # Get the id of the selected row
        self.selectedId = curValues[0]
        print ('Selected Id = ' + str(self.selectedId))

        self.update_title.insert(0, curValues[1])
        self.update_body.insert(0, curValues[2])
        self.update_paragraph.insert(0, curValues[3])
        self.update_footer.insert(0, curValues[4])

    def onDelete(self):
        # Delete the HTML entry
        title = self.update_title.get()
        body = self.update_body.get()
        paragraph = self.update_paragraph.get()
        footer = self.update_footer.get()

        db_program.deleteHTML(self.selectedId)

        # Refresh the table
        self.updateTreeView()

        # Empty text boxes when finished.
        self.update_title.delete(0, END)
        self.update_body.delete(0, END)
        self.update_paragraph.delete(0, END)
        self.update_footer.delete(0, END)

        # Update tree view
        self.updateTreeView()

    def updateTreeView(self):
        # Get data from the database
        self.allData = db_program.viewAll()

        # Delete old data before adding new data
        for i in self.htmlTree.get_children():
            self.htmlTree.delete(i)

        # Append data to the table
        html_list= db_program.viewAll()

        for item in html_list:
            self.htmlTree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)

        #Clean out the update text boxes
        self.update_title.delete(0, END)
        self.update_body.delete(0, END)
        self.update_paragraph.delete(0, END)
        self.update_footer.delete(0, END)

def sortby(htmlTree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(htmlTree.set(child, col), child) \
        for child in htmlTree.get_children('')]
    # if the data to be sorted is numeric change to float
    #data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        htmlTree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    htmlTree.heading(col, command=lambda col=col: sortby(htmlTree, col, \
        int(not descending)))

html_header = ['ID', 'Heading', 'Body', 'Paragraph', 'Footer']

def main():

    root = Tk()
    htmlBuild = HTMLBuild(root)
    root.mainloop()
    
if __name__ == "__main__": main()
