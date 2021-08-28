from tflite_runtime.interpreter import Interpreter 
from PIL import Image
import numpy as np
import time
import tkinter as tk
from tkinter import *
from tkinter.font import families
import tkinter.font as font
from PIL import ImageTk, Image

'''
* Drying Countdown Timing before ML
* Page 4 of the GUI
* @Author June Han
'''

class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Create a frame
        frame = LabelFrame(self, padx=50, pady=50)
        frame.pack(padx=10, pady=10)

        #=================================================Functions=============================================================================
        #Restart Cleaning
        def ReStart():
            controller.show_frame("Page2")

        #Proceed to Sterilise
        def Sterilise():
            controller.show_frame("Page5")

        def load_labels(path): # Read the labels from the text file as a Python list.
            with open(path, 'r') as f:
                return [line.strip() for i, line in enumerate(f.readlines())]

        def set_input_tensor(interpreter, image):
            tensor_index = interpreter.get_input_details()[0]['index']
            input_tensor = interpreter.tensor(tensor_index)()[0]
            input_tensor[:, :] = image

        def classify_image(interpreter, image, top_k=1):
            set_input_tensor(interpreter, image)

            interpreter.invoke()
            output_details = interpreter.get_output_details()[0]
            output = np.squeeze(interpreter.get_tensor(output_details['index']))

            scale, zero_point = output_details['quantization']
            output = scale * (output - zero_point)

            ordered = np.argpartition(-output, 1)
            return [(i, output[i]) for i in ordered[:top_k]][0]
        #=================================================Functions END=============================================================================

        self.configure(background='#FBF6F3')

        #Create a label for cleaning title
        cleaningFont = font.Font(family = 'Kristen ITC', size=25, weight='bold')
        label1 = Label(frame, text = "Cleaning Completed...", bg="#FBF6F3")
        label1['font'] = cleaningFont
        label1.pack(padx=50, pady=5, anchor=W)

        #=================================================ML_Check=============================================================================
        #Create an image space
        MLimage = Image.open("testSyringe3.jpg")
        MLimage = MLimage.resize((224, 224), Image.ANTIALIAS)
        ML_img = ImageTk.PhotoImage(MLimage)
        Label2 = Label(frame, image=ML_img)
        Label2.pack()
        
        data_folder = "./"

        model_path = data_folder + "mobilenet_v2_1.0_224_quant.tflite"
        label_path = data_folder + "syringe_labels.txt"

        interpreter = Interpreter(model_path)
        print("Model Loaded Successfully.")


        interpreter.allocate_tensors()
        _, height, width, _ = interpreter.get_input_details()[0]['shape']
        print("Image Shape (", width, ",", height, ")")

        # Load an image to be classified.
        image = Image.open(data_folder + "testSyringe3.jpg").convert('RGB').resize((width, height))

        # Classify the image.
        time1 = time.time()
        label_id, prob = classify_image(interpreter, image)
        time2 = time.time()
        classification_time = np.round(time2-time1, 3)
        print("Classification Time =", classification_time, "seconds.")

        # Read class labels.
        labels = load_labels(label_path)

        # Return the classification label of the image.
        classification_label = labels[label_id]
        print("Image Label is :", classification_label, ", with Accuracy :", prob, "%.")
        

        #Status Label
        StatusFont = font.Font(family = 'Kristen ITC', size=20, weight='bold')
        StatusLabel = Label(frame, text=classification_label, padx = 140, pady = 10, bg="#FBF6F3", relief=SUNKEN)
        StatusLabel['font'] = StatusFont
        StatusLabel.pack(padx=50, pady=5, anchor=CENTER)
        #=================================================ML_Check=============================================================================

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