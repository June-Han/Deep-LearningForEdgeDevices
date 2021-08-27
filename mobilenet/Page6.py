from tkinter import *
from tkinter.font import families
import tkinter.font as font

'''
* Sterilisation completed
* Page 6 of the GUI
* @Author June Han
'''

#create root widget for a window
rootwindow = Tk()
rootwindow.title("Syringe Washer UI")
rootwindow.iconbitmap("./syringe.ico")

#Create a frame
frame = LabelFrame(rootwindow, padx=50, pady=50)
frame.pack(padx=10, pady=10)

def Retrieve():
    rootwindow.destroy()
    import Page1

#Set window background
rootwindow.configure(background='#FBF6F3')

#Create a label for drying title
SteriliseFont = font.Font(family = 'Kristen ITC', size=25, weight='bold')
label1 = Label(frame, text = "Sterilisation Completed", bg="#FBF6F3")
label1['font'] = SteriliseFont
label1.pack(padx=50, pady=5, anchor=CENTER)


# Create Exit Button
ExitButtonFont = font.Font(family = 'Kristen ITC', size=25, weight='bold')
ExitButton = Button(frame, text="RETRIEVE", padx = 100, pady = 10, fg="white", bg="#72C64B", command= lambda: Retrieve())
ExitButton['font'] = ExitButtonFont
ExitButton.pack(padx=50, pady=5, anchor=CENTER)


rootwindow.mainloop()