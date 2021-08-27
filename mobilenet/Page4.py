from tkinter import *
from tkinter.font import families
import tkinter.font as font
from PIL import ImageTk, Image

'''
* Drying Countdown Timing before ML
* Page 4 of the GUI
* @Author June Han
'''

#create root widget for a window
rootwindow = Tk()
rootwindow.title("Syringe Washer UI")
rootwindow.iconbitmap("./syringe.ico")

#Create a frame
frame = LabelFrame(rootwindow, padx=50, pady=50)
frame.pack(padx=10, pady=10)

#Restart Cleaning
def ReStart():
    rootwindow.destroy()
    import Page2

#Proceed to Sterilise
def Sterilise():
    rootwindow.destroy()
    import Page5

#Set the geometry center
screen_width = rootwindow.winfo_screenwidth()
screen_height = rootwindow.winfo_screenheight()
rootwindow.configure(background='#FBF6F3')

#Create a label for cleaning title
cleaningFont = font.Font(family = 'Kristen ITC', size=25, weight='bold')
label1 = Label(frame, text = "Cleaning Completed...", bg="#FBF6F3")
label1['font'] = cleaningFont
label1.pack(padx=50, pady=5, anchor=W)

#Create an image space
image = Image.open("testSyringe3.jpg")
image = image.resize((224, 224), Image.ANTIALIAS)
ML_img = ImageTk.PhotoImage(image)
Label2 = Label(frame, image=ML_img)
Label2.pack()

#Status Label
countdownFont = font.Font(family = 'Kristen ITC', size=20, weight='bold')
StatusLabel = Label(frame, text="Status", padx = 140, pady = 10, bg="#FBF6F3", relief=SUNKEN)
StatusLabel['font'] = countdownFont
StatusLabel.pack(padx=50, pady=5, anchor=CENTER)


#Create Restart washing Button
ReStartButtonFont = font.Font(family = 'Kristen ITC', size=25, weight='bold')
ReStartButton = Button(frame, text="RE-WASH", padx = 100, pady = 10, fg="white", bg="red", command= lambda: ReStart())
ReStartButton['font'] = ReStartButtonFont
ReStartButton.pack(padx=50, pady=5, anchor=CENTER)

# Create Process to Sterilise Button
ButtonFont = font.Font(family = 'Kristen ITC', size=25, weight='bold')
ExitButton = Button(frame, text="CONTINUE", padx = 80, pady = 10, fg="white", bg="#72C64B", command= lambda: Sterilise())
ExitButton['font'] = ButtonFont
ExitButton.pack(padx=50, pady=5, anchor=CENTER)


rootwindow.mainloop()