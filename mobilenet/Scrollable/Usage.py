import tkinter as tk
from tkinter import ttk
from ScrollableFrameClass import Scrollable

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        sbf = Scrollable(self)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        sbf.grid(row=0, column=0, sticky='nsew')
        # sbf.pack(side="top", fill="both", expand=True)

        # Some data, layout into the sbf.scrolled_frame
        frame = sbf.scrolled_frame
        for row in range(50):
            text = "%s" % row
            tk.Label(frame, text=text,
                     width=3, borderwidth="1", relief="solid") \
                .grid(row=row, column=0)

            text = "this is the second column for row %s" % row
            tk.Label(frame, text=text,
                     background=sbf.scrolled_frame.cget('bg')) \
                .grid(row=row, column=1)


if __name__ == "__main__":
    App().mainloop()