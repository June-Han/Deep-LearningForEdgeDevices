from tkinter import *
from tkinter.font import families
import tkinter.font as font
from tkinter_custom_button import TkinterCustomButton

#create root widget for a window
rootwindow = Tk()
rootwindow.title("Syringe Washer UI")
rootwindow.iconbitmap("./syringe.ico")

def afterStart():
    rootwindow.destroy()
    import Page2

#Set the geometry center
screen_width = rootwindow.winfo_screenwidth()
screen_height = rootwindow.winfo_screenheight()

rootwindow.geometry("{0}x{1}".format(screen_width-100, screen_height-100))

rootwindow.configure(background='#FBF6F3')

#Create a label
welcomeFont = font.Font(family = 'Kristen ITC', size=50, weight='bold')
label1 = Label(rootwindow, text = "Page2", bg="#FBF6F3")
label1['font'] = welcomeFont
label1.place(relx=0.5, rely=0.3, anchor=CENTER)

#Create Button
reStartButtonFont = font.Font(family = 'Kristen ITC', size=25, weight='bold')
reStartButton = Button(rootwindow, text="RE-START", padx = 60, pady = 10, fg="white", bg="red")
##57DDF3
reStartButton['font'] = reStartButtonFont
reStartButton.place(relx=0.5, rely=0.5, anchor=CENTER)

#Create Button
ContinueButtonFont = font.Font(family = 'Kristen ITC', size=25, weight='bold')
ContinueButton = Button(rootwindow, text="CONTINUE", padx = 50, pady = 10, fg="white", bg="#72C64B")
##57DDF3
ContinueButton['font'] = ContinueButtonFont
ContinueButton.place(relx=0.5, rely=0.65, anchor=CENTER)

rootwindow.mainloop()