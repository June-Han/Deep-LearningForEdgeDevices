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

def ExitApp():
    rootwindow.destroy()

#Set the geometry center
screen_width = rootwindow.winfo_screenwidth()
screen_height = rootwindow.winfo_screenheight()

rootwindow.geometry("{0}x{1}".format(screen_width-100, screen_height-100))

rootwindow.configure(background='#FBF6F3')

#Create a label
welcomeFont = font.Font(family = 'Kristen ITC', size=50, weight='bold')
label1 = Label(rootwindow, text = "Welcome", bg="#FBF6F3")
label1['font'] = welcomeFont
label1.place(relx=0.5, rely=0.45, anchor=CENTER)

#Create Start Button
StartButtonFont = font.Font(family = 'Kristen ITC', size=25, weight='bold')
StartButton = Button(rootwindow, text="START WASH", padx = 60, pady = 10, fg="white", bg="#72C64B", command= lambda: afterStart())
##57DDF3
StartButton['font'] = StartButtonFont
StartButton.place(relx=0.5, rely=0.55, anchor=CENTER)

# Create Exit Button
ExitButtonFont = font.Font(family = 'Kristen ITC', size=25, weight='bold')
ExitButton = Button(rootwindow, text="EXIT", padx = 60, pady = 10, fg="white", bg="red", command= lambda: afterStart())
##57DDF3
ExitButton['font'] = StartButtonFont
ExitButton.place(relx=0.5, rely=0.66, anchor=CENTER)

rootwindow.mainloop()