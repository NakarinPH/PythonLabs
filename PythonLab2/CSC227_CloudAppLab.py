# Nakarin Philangam
# This program create a GUI that convert fahrenheit to celsius by the number that the user input

import tkinter


class CelsiusConvertorGui:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # Add a title for the GUI
        self.main_window.title("Fahrenheit to Celsius Convertor")

        # Set the size of the main window
        self.main_window.geometry('250x125')

        # Create frames to group widgets
        self.fahrenheit_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        # Create the widgets for the fahrenheit_frame
        self.fahrenheit_label = tkinter.Label(self.fahrenheit_frame,
                                              text='Enter Fahrenheit: ')
        self.fahrenheit_entry = tkinter.Entry(self.fahrenheit_frame,
                                              width=10)

        # Pack the fahrenheit_frame's widgets
        self.fahrenheit_label.pack(side='left')
        self.fahrenheit_entry.pack(side='left')

        # Create the widgets for the result_frame
        self.result_label = tkinter.Label(self.result_frame,
                                          text='Celsius = ')

        # Use the object's set method to store a string of blank characters
        self.result_value = tkinter.StringVar()

        # Create a label and associate it with the String Object.
        self.result_value_label = tkinter.Label(self.result_frame,
                                                textvariable=self.result_value)

        # Pack the widgets for button_frame
        self.result_label.pack(side='left')
        self.result_value_label.pack(side='left')

        # Create the widgets for button_frame
        self.convert_button = tkinter.Button(self.button_frame,
                                             text='Convert',
                                             command=self.convert)
        self.cancel_button = tkinter.Button(self.button_frame,
                                            text='Cancel',
                                            command=self.main_window.destroy)

        # Pack the buttons
        self.convert_button.pack(side='left')
        self.cancel_button.pack(side='left')

        # Pack the frames
        self.fahrenheit_frame.pack()
        self.result_frame.pack()
        self.button_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    def convert(self):
        # Get the value entered by the user into the fahrenheit_entry
        fahrenheit_number = float(self.fahrenheit_entry.get())

        # Convert fahrenheit to celsius
        celsius = (fahrenheit_number - 32) * 5 / 9

        # Convert result_value to a string and store it in the StringVar Object
        self.result_value.set(celsius)


# Create an instance of the CelsiusConvertorGui class
fahrenheit_convertor = CelsiusConvertorGui()
