import tkinter

window = tkinter.Tk()

window.title("Main Window")
window.minsize(1440, 900)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()
# my_label.pack(side="left")
# my_label.pack(expand=1)
my_label["text"] = "Yo!!!"


# Button
def button_clicked():
    new_label = input.get()
    my_label.config(text=new_label)


button = tkinter.Button(text="Click Me!", command=button_clicked)
button.pack()

# Entry

input = tkinter.Entry(width=10)
input.pack()



# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     print(total)
#
#
# add(1, 2, 3, 4)
#
# def calculate(**kwargs):
#     for key, value in kwargs.items():
#         print(key)
#     print(kwargs["multiply"])
#
#
# calculate(add=3, multiply=5)

window.mainloop()