
from Tkinter import *
import ttk
import time
from datetime import datetime, timedelta


class Feedback:

    def __init__(self, master):
        
        master.title('Our Office Clocks')
        master.resizable(False, False)
        master.configure(background = '#FFEB99')
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#FFEB99')
        self.style.configure('TButton', background = '#FFEB99')
        self.style.configure('TLabel', background = '#FFEB99', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))      

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
        ttk.Label(self.frame_header, text = 'Welcome to the office', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, 
                  text = ("Our Office Hours are from 9:00 AM to 9:00 PM")).grid(row = 1, column = 1)
        
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Location').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Time').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Open/Closed').grid(row = 0, column = 2, padx = 5, sticky = 'sw')

        nineAM = "0900"
        ninePM = "2100"
        
        self.PDXTime = time.strftime("%I:%M %p")
        nowAtPDX = time.strftime("%H%M")

        self.PDXOpenClosed = "Closed"
        if nowAtPDX >= nineAM and nowAtPDX <= ninePM:
            self.PDXOpenClosed = "Open"
                                 
        current_plus_three = datetime.now() + timedelta(hours=3)
        self.NYTime = format(current_plus_three, "%I:%M %p")

        nowPlusThree = format(current_plus_three, "%H%M")
        self.NYOpenClosed = "Closed"
        if nowPlusThree >= nineAM and nowPlusThree <= ninePM:
            self.NYOpenClosed = "Open"

        current_plus_eight = datetime.now() + timedelta(hours=8)
        self.UKTime = format(current_plus_eight, "%I:%M %p")

        nowPlusEight = format(current_plus_eight, "%H%M")
        self.UKOpenClosed = "Closed"
        if nowPlusEight >= nineAM and nowPlusEight <= ninePM:
            self.UKOpenClosed = "Open"
        
        
        ttk.Label(self.frame_content, text = 'Portland, OR').grid(row = 1, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'New York').grid(row = 2, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'London').grid(row = 3, column = 0, padx = 5, sticky = 'sw')

        ttk.Label(self.frame_content, text = self.PDXTime).grid(row = 1, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = self.NYTime).grid(row = 2, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = self.UKTime).grid(row = 3, column = 1, padx = 5, sticky = 'sw')

        ttk.Label(self.frame_content, text = self.PDXOpenClosed).grid(row = 1, column = 2, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = self.NYOpenClosed).grid(row = 2, column = 2, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = self.UKOpenClosed).grid(row = 3, column = 2, padx = 5, sticky = 'sw')
        

         
 #       self.PDXTime(self.frame_Content.grid(row = 1, column = 1, padx = 5)
 #       self.NYTime.grid(row = 2, column = 1, padx = 5)
 #       self.UKTime.grid(row = 3, column = 1, padx = 5)
          
def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()
