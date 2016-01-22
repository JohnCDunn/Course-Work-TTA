
__author__ = 'Student'
from Tkinter import *
import ttk
import shutil
import os
import time
from datetime import datetime, timedelta
import sqlite3




class MoveEm():

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

        lastDateTime = ''.join(getLastUpdate())

        ttk.Label(self.frame_header, text = 'Welcome to the File Transfer 2', style = 'Header.TLabel').grid(row = 0, column = 1)
        label2 = ttk.Label(self.frame_header, text = 'Last transferred on ' + lastDateTime, style = 'Header.TLabel').grid(row = 1, column = 1)

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

        updateLastUpdate(self)

def getLastUpdate():
    #connect to the database
    conn = sqlite3.connect('time_database.db')

    #open a cursor
    c = conn.cursor()

    #execute sql to get last_update date and time
    c.execute("SELECT last_datetime FROM time_table limit 1")

    #get the last update date and time
    #this is a tuple
    last_updt = c.fetchone()

    #change last_updt to a string
    #last_updt_str = "".join(last_updt)

    #close the connection
    conn.close()

    return last_updt

def updateLastUpdate(self):

    #create a db connection to the time_database
    conn = sqlite3.connect('time_database.db')

    #open a cursor
    c=conn.cursor()

    #get current date and time formatted
    currDateTime = format(datetime.now(), "%Y-%m-%d %H:%M:%S")
    updateID = "1"

    #execute sql to update the datetime stamp
    c.execute("UPDATE time_table SET last_datetime = ? WHERE last_update=?", (currDateTime, updateID))

    #commit the changes
    conn.commit()

    #close the connection
    conn.close()

def main():

    root = Tk()
    feedback = MoveEm(root)
    root.mainloop()

if __name__ == "__main__": main()
