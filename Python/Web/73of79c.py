#!/usr/bin/python3
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Feedback:

    def __init__(self, master):
        
        master.title('Build A Body')
        master.resizable(False, False)
        master.configure(background = '#e1d8b9')
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#e1d8b9')
        self.style.configure('TButton', background = '#e1d8b9')
        self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))      

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
    
        ttk.Label(self.frame_header, wraplength = 300, text='').grid(row = 1, column = 1)
               
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

       
        ttk.Label(self.frame_content, text = 'Enter Body text below:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')
        
      
        self.text_body = Text(self.frame_content, width = 50, height = 1, font = ('Arial', 10))

             
        self.text_body.grid(row = 3, column = 0, columnspan = 2, padx = 5)

        
        ttk.Button(self.frame_content, text = 'Generate HTML',
                   command = self.processHTML).grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'sw')
      

    def processHTML(self):

        import webbrowser
        f = open('Python_HTML.html','w')

        bodyText = self.text_body.get(1.0, 'end')

        wrapper = """
        <html>
        <body>
        %s
        </body>
        </html>"""

        message = wrapper % (bodyText)

        f.write(message),bodyText
        f.close()

        webbrowser.open_new_tab('Python_HTML.html')
         
def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()
