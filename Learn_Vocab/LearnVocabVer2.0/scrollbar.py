from tkinter import *
from tkinter import ttk

class scroll:
    def __init__(self,root):
        # Create a main frame
        self.mainFrame=Frame(root)
        self.mainFrame.pack(fill=BOTH, expand=1)
        # Create a canvas
        self.myCanvas=Canvas(self.mainFrame)
        self.myCanvas.pack(side=LEFT, fill=BOTH, expand=1)
        # Add a scrollbar to the canvas
        self.myScrollbar=ttk.Scrollbar(self.mainFrame, orient=VERTICAL,command=self.myCanvas.yview)
        self.myScrollbar.pack(side=RIGHT, fill=Y)
        # Configure the canvas
        self.myCanvas.configure(yscrollcommand=self.myScrollbar.set)
        self.myCanvas.bind('<Configure>', lambda e: self.myCanvas.configure(scrollregion=self.myCanvas.bbox("all")))
        # Create second frame
        self.ndFrame=Frame(self.myCanvas)
        # Add that new frame to a window in the canvas
        self.myCanvas.create_window((0,0), window=self.ndFrame,anchor=NW)