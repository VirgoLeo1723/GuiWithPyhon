from tkinter import *
from tkinter import ttk

class scrollbarSetting:
    @staticmethod
    def Setting(root):
        # Create a main frame
        mainFrame=Frame(root)
        mainFrame.pack(fill=BOTH, expand=1)
        # Create a canvas
        myCanvas=Canvas(mainFrame)
        myCanvas.pack(side=LEFT, fill=BOTH, expand=1)
        # Add a scrollbar to the canvas
        myScrollbar=ttk.Scrollbar(mainFrame, orient=VERTICAL,command=myCanvas.yview)
        myScrollbar.pack(side=RIGHT, fill=Y)
        # Configure the canvas
        myCanvas.configure(yscrollcommand=myScrollbar.set)
        myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox("all")))
        # Create second frame
        ndFrame=Frame(myCanvas)
        # Add that new frame to a window in the canvas
        myCanvas.create_window((0,0), window=ndFrame,anchor=NW)
        
        for number in range(0,100):
            Button(ndFrame,text="Label "+str(number),width=10).grid(row=number, column=0)

        root.mainloop()