# Whatever you enter in text box will appear in label after clicking on button.
from tkinter import *

windows = Tk()
windows.title("GUI Program")
windows.minsize(width=600, height=600)

def button_function():
    my_label.config(text=input.get())


# Label
my_label = Label(text="I am a Label")
my_label.config(text="Configured my text")  # To change existing text
my_label.pack()

# Button
button = Button(text="Hit me", command=button_function)
button.pack()

# Entry - input text box
input = Entry()
input.pack()


windows.mainloop()
