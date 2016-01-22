from Tkinter import *
import ttk
import shutil
import os


class MoveEm:

    def __init__(self, master):

                
        master.title('File Shuttle 1')
        master.resizable(False, False)
        master.configure(background = '#00CED1')
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#00CED1')
        self.style.configure('TButton', background = '#00CED1')
        self.style.configure('TLabel', background = '#00CED1', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))      

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
        ttk.Label(self.frame_header, text = 'Welcome to the File Transfer', style = 'Header.TLabel').grid(row = 0, column = 1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        b1 = Button(self.frame_content,text="Click here to move all files between Folder A and Folder B", command=self.moveFiles)
        b1.pack()

        b1.grid(row=3, column=0)


    def moveFiles (self):

        aCount = 0
        bCount = 0

        dir_A = "C:\Users\Student\Desktop\Folder A"
        dir_B = "C:\Users\Student\Desktop\Folder B"
        for file in os.listdir(dir_A):
            aCount = aCount + 1
        for file in os.listdir(dir_B):
            bCount = bCount + 1
        print (aCount, bCount)

        if aCount > 0:
            to_dir = dir_B
            from_dir = dir_A

        if bCount > 0:
            to_dir = dir_A
            from_dir = dir_B

        for file in os.listdir(from_dir):
            print ("from file = " + from_dir + file)
            from_file = os.path.join(from_dir, file)
            to_file = os.path.join(to_dir, file)
            print ("to file = " + to_dir + file)
            shutil.move(from_file, to_file)



def main():            
    
    root = Tk()
    feedback = MoveEm(root)
    root.mainloop()

if __name__ == "__main__": main()
