from tkinter import *
from tkinter.font import families
import tkinter.font as font

'''
* Welcome Page
* Page 1 of the GUI
* @Author June Han
'''

#create root widget for a window
rootwindow = Tk()
rootwindow.title("Syringe Washer UI")
rootwindow.iconbitmap("./syringe.ico")

#Create a frame
frame = LabelFrame(rootwindow, padx=50, pady=50)
frame.pack(padx=10, pady=10)

#Function to run after starting the program
def afterStart():
    rootwindow.destroy()
    import Page2

#Exit the program
def ExitApp():
    #rootwindow.quit()
    rootwindow.quit()

#Set the geometry center
screen_width = rootwindow.winfo_screenwidth()
screen_height = rootwindow.winfo_screenheight()
#rootwindow.geometry("{0}x{1}".format(screen_width-100, screen_height-100))

rootwindow.configure(background='#FBF6F3')

#Create a label
welcomeFont = font.Font(family = 'Kristen ITC', size=50, weight='bold')
label1 = Label(frame, text = "Welcome", bg="#FBF6F3")
label1['font'] = welcomeFont
#label1.place(relx=0.5, rely=0.45, anchor=CENTER)
label1.pack(padx=50, pady=5, anchor=CENTER)

#Create Start Button
StartButtonFont = font.Font(family = 'Kristen ITC', size=25, weight='bold')
StartButton = Button(frame, text="START WASH", padx = 60, pady = 10, fg="white", bg="#72C64B", command= lambda: afterStart())
StartButton['font'] = StartButtonFont
#StartButton.place(relx=0.5, rely=0.55, anchor=CENTER)
StartButton.pack(padx=50, pady=5, anchor=CENTER)

# Create Exit Button
ExitButtonFont = font.Font(family = 'Kristen ITC', size=25, weight='bold')
ExitButton = Button(frame, text="EXIT", padx = 142, pady = 10, fg="white", bg="red", command= lambda: ExitApp())
ExitButton['font'] = StartButtonFont
#ExitButton.place(relx=0.5, rely=0.66, anchor=CENTER)
ExitButton.pack(padx=50, pady=5, anchor=CENTER)

rootwindow.mainloop()