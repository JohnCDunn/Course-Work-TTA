__author__ = 'Student'
from Tkinter import *
import ttk
import shutil
import os
import time
from datetime import datetime, timedelta
import sqlite3




class MoveEm:

    def __init__(self, master):

        master.title('File Shuttle 2')
        master.resizable(False, False)
        master.configure(background = '#00CED1')

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#00CED1')
        self.style.configure('TButton', background = '#00CED1')
        self.style.configure('TLabel', background = '#00CED1', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        sqlite_file = 'time_database.db'
        table_name = 'time_table'

        conn = sqlite3.connect("time_database.db")
        r = conn.cursor()

        lastDateTime = r.execute("SELECT last_update FROM time_table")

        ttk.Label(self.frame_header, text = 'Welcome to the File Transfer 2', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, text = 'Welcome to the File Transfer 2', style = 'Header.TLabel').grid(row = 0, column = 1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        b1 = Button(self.frame_content,text="Click here to move files changed in the last 24 hours from Folder A to Folder B", command=self.moveFiles)
        b1.pack()

        b1.grid(row=3, column=0)


    def moveFiles (self):

        #establish dates
        yesterday = datetime.now() + timedelta(hours=-24)
        dateTime_24  = format(yesterday, "%Y%m%d")
        dateTimeNow = time.strftime("%Y%m%d")

        dir_A = "C:\Users\Student\Desktop\Folder A"
        dir_B = "C:\Users\Student\Desktop\Folder B"

        for file in os.listdir(dir_A):

            #define the complete path for the file
            filePathA = os.path.join(dir_A,file)
            fileDateTime = time.strftime('%Y%m%d', time.gmtime(os.path.getmtime(filePathA)))

            if (fileDateTime >= dateTime_24 and
                fileDateTime <= dateTimeNow):
                filePathB = os.path.join(dir_B,file)
                shutil.move(filePathA, filePathB)


def main():

    root = Tk()
    feedback = MoveEm(root)
    root.mainloop()

if __name__ == "__main__": main()
