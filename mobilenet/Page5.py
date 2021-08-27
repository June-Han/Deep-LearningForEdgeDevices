from tkinter import *
from tkinter.font import families
import tkinter.font as font

'''
* Sterilisation Countdown Timing before Retrieving Syringes
* Page 5 of the GUI
* @Author June Han
'''

#create root widget for a window
rootwindow = Tk()
rootwindow.title("Syringe Washer UI")
rootwindow.iconbitmap("./syringe.ico")

#Create a frame
frame = LabelFrame(rootwindow, padx=50, pady=50)
frame.pack(padx=10, pady=10)

def StopDrying():
    rootwindow.destroy()
    import Page1

#Create a function for countdown
def countdown(seconds):
    hours, remainder = divmod(seconds, 3600)
    mins, secs = divmod(remainder, 60)
    timeformat = "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)
    timeLabel.config(text=timeformat)
    seconds -=1
    #When second is 0, it will be -1.
    if (seconds == -1):
        rootwindow.destroy()
        import Page6
    else:
        # call function again after 1000ms (1s)
        frame.after(1000,lambda: countdown(seconds))

#Set the geometry center
screen_width = rootwindow.winfo_screenwidth()
screen_height = rootwindow.winfo_screenheight()
rootwindow.configure(background='#FBF6F3')

#Create a label for drying title
SteriliseFont = font.Font(family = 'Kristen ITC', size=25, weight='bold')
label1 = Label(frame, text = "Sterilizing...", bg="#FBF6F3")
label1['font'] = SteriliseFont
label1.pack(padx=50, pady=5, anchor=W)

#Countdown Label
countdownFont = font.Font(family = 'Kristen ITC', size=20, weight='bold')
timeLabel = Label(frame, text=0, padx = 140, pady = 10, bg="#FBF6F3", relief=SUNKEN)
timeLabel['font'] = countdownFont
timeLabel.pack(padx=50, pady=5, anchor=CENTER)
countdown(10)


# Create Exit Button
ExitButtonFont = font.Font(family = 'Kristen ITC', size=25, weight='bold')
ExitButton = Button(frame, text="STOP", padx = 140, pady = 10, fg="white", bg="red", command= lambda: StopDrying())
ExitButton['font'] = ExitButtonFont
ExitButton.pack(padx=50, pady=5, anchor=CENTER)


rootwindow.mainloop()