from tkinter import *


def button_calculate():
    # print("I got clicked")
    # new_text = input.get()
    # my_label.config(text=new_text)
    converted = float(input_miles.get()) * 1.609
    label_km_ct.config(text=f"{converted}")


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

label_miles = Label(text="Miles", font=("Arial", 12, "bold"))
label_is_eq = Label(text="is equal to", font=("Arial", 12, "bold"))
label_km_ct = Label(text="0", font=("Arial", 12, "bold"))
label_kilos = Label(text="Km", font=("Arial", 12, "bold"))

label_miles.grid(column=3, row=0)
label_is_eq.grid(column=0, row=1)
label_km_ct.grid(column=1, row=1)
label_kilos.grid(column=2, row=1)

button_calc = Button(text="Calculate", command=button_calculate)
button_calc.grid(column=1, row=2)


#Entry
input_miles = Entry(width=10)
input_miles.grid(column=1, row=0)

window.mainloop()
