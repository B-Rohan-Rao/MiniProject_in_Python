from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer")
window.config(padx=30, pady=30)

miles_input = Entry(width=5)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equals_label = Label(text="is equals to:")
is_equals_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer = Label(text="Km")
kilometer.grid(column=2, row=1)

calculate = Button(text="calculate", command=miles_to_km)
calculate.grid(column=1, row=2)

window.mainloop()
