import tkinter as tk
root = tk.Tk()

a = tk.Label(root,text="")
a.pack()

def set_idle_timer(t):
    hours, remainder = divmod(t, 3600)
    mins, secs = divmod(remainder, 60)
    timeformat = "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)
    a.config(text=timeformat)
    t -=1
    root.after(1000,lambda: set_idle_timer(t))

set_idle_timer(3600)

root.mainloop()