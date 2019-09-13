# This program calculates the windchill temperature using temperature without windchill and wind speed
# Author: Zaid Yazadi

# imports tkinter module
from tkinter import *

# Creates GUI class
class WindGUI:
    # Builds the GUI
    def __init__(self):
        # Creates the window and frames
        self.window = Tk()
        self.frame1 = Frame()
        self.frame2 = Frame()
        self.frame3 = Frame()

        # Creates the labels for the title, temperature prompt, and speed prompt
        self.title = Label(self.frame1, text="Windchill Calculator", font='Helvetica 12 bold')
        self.temp = Label(self.frame1, text="Enter the temperature in degrees Fahrenheit")
        self.speed = Label(self.frame2, text="Enter the wind speed in mph")

        # Creates the Entry widgets for temperature and speed
        self.tempEntry = Entry(self.frame1, width=3)
        self.speedEntry = Entry(self.frame2, width=3)

        # Creates the calculate button that uses the calculate_windchill function
        self.calculateBtn = Button(self.frame3, text="Calculate", command=self.calculate_windchill)

        # Creates the output label that displays the calculated windchill temperature
        self.description = Label(self.frame3, text="The windchill temperature is:")
        self.value = StringVar()
        self.windchill = Label(self.frame3, textvariable=self.value)

        # Packs all the widgets in the proper format
        self.title.pack(side='top')
        self.temp.pack(side='left')
        self.tempEntry.pack(side='left')
        self.speed.pack(side='left')
        self.speedEntry.pack(side='left')
        self.calculateBtn.pack(side='top')
        self.description.pack(side='left')
        self.windchill.pack(side='left')

        # Packs all the frames in the proper sequence
        self.frame1.pack(side='top')
        self.frame2.pack()
        self.frame3.pack()

        # Makes sure GUI runs until exited out of
        mainloop()

    # Function to calculate windchill temperature
    # Gets entry values, calculates windchill, and sets self.value to windchill value
    # Var temperature, wind_speed, windchill
    def calculate_windchill(self):
        temperature = float(self.tempEntry.get())
        wind_speed = float(self.speedEntry.get())
        windchill = 35.74 + (0.6215 * temperature) - (35.75 * wind_speed ** 0.16) + (
                0.4275 * temperature * wind_speed ** 0.16)

        self.value.set(format(windchill, '.1f'))


# Creates instance of WindGUI so program will run
wcGUI = WindGUI()
