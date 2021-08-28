import tkinter as tk
from tkinter import * 
from tkinter.font import families
import tkinter.font as font
from Page1 import Page1
from Page2 import Page2
from Page3 import Page3
from Page4 import Page4
from Page5 import Page5
from Page6 import Page6

class SyringeApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Syringe Washer UI")
        self.iconbitmap("./syringe.ico")

        self.title_font = font.Font(family='Kristen ITC', weight="bold")

        #The container is a window where we'll change the frames
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        '''
        for F in (Page1, Page2, Page3, Page4, Page5, Page6):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        '''
        #Create a mapping from string Page_Name: Page
        for F in (Page1, Page2, Page3, Page4, Page5, Page6):
            page_name = F.__name__
            self.frames[page_name] = F
        
        self.show_frame("Page1")

    def show_frame(self, page_name):
        '''
        #Destroy any old frame
        if len(self.container.winfo_children()) != 0:
            for child in self.container.winfo_children():
                child.destroy()
        '''
        for l in self.container.slaves():
            l.destroy()
        # create the new frame
        frame_class = self.frames[page_name]
        frame = frame_class(parent=self.container, controller = self)
        frame.grid(row=0, column=0, sticky="nsew")
        '''
        #Will expand till beyond the screen lol
        frame.pack(fill="both", expand=True) 
        '''
        """
        #Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()
        """


if __name__ == "__main__":
    app = SyringeApp()
    app.mainloop()