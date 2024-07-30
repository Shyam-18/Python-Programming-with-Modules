from tkinter import *

windows = Tk()
windows.title("Mile to Km Converter")
windows.configure(padx=20, pady=20)


def converter():
    input1 = int(miles_input.get()) * 1.6
    km_label.config(text=input1)


equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

miles_input = Entry()
miles_input.grid(column=1, row=0)

km_label = Label(text="__")
km_label.grid(column=1, row=1)

button = Button(text="Calculate", command=converter)
button.grid(column=1,row=2)

windows.mainloop()
