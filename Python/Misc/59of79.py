''' tk_LabelFrame_grid_layout1.py
grid layout of frames
'''
# Python3
import tkinter as tk
root = tk.Tk()
root.geometry("500x600")
frame1 = tk.LabelFrame(root, text="frame1", width=150, height=200, bd=5)
frame2 = tk.LabelFrame(root, text="frame2", width=150, height=200, bd=5)
frame3 = tk.LabelFrame(root, text="frame3", width=300, height=300, bd=5)

frame1.grid(row=0, column=0, padx=8)
frame2.grid(row=1, column=0, padx=8)
frame3.grid(row=0, column=2, rowspan=2, sticky='nw')

root.mainloop()