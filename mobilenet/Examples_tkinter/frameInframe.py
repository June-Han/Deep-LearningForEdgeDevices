import tkinter as Tkinter

tk = Tkinter.Tk()
frame1 = Tkinter.Frame(tk, padx = 150, pady = 150, bg = "WHITE", borderwidth=2)
frame2 = Tkinter.Frame(frame1, padx = 80, pady = 80, bg = "RED", borderwidth=2)
frame1.pack()
frame2.pack()
button = Tkinter.Button(frame1,text="Button") #Send some action to Label here
button.pack()
label = Tkinter.Label(frame2, text = "Label") #Receive a callback from button here
label.pack()
tk.mainloop()   