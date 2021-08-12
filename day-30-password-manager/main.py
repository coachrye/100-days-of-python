from tkinter import *
from tkinter import messagebox
import pyperclip  # For automatic copy-paste
import json

FONT_NAME = "Arial"
DEFAULT_EMAIL = "rye@coachrye.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)

    input_pass.delete(0, END)
    input_pass.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    site = input_site.get()
    try:
        with open("data.json", "r") as pass_file:
            data = json.load(pass_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found.")
    else:
        if site in data:
            email = data[site]['email']
            password = data[site]['password']
            messagebox.showinfo(title="Oops", message=f"Website: {site}"
                                                      f"\nEmail: {email}"
                                                      f"\nPassword:{password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Oops", message=f"No details for {site} exists.")



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    save_site = input_site.get()
    save_user = input_user.get()
    save_pass = input_pass.get()
    new_data = {
        save_site: {
            "email": save_user,
            "password": save_pass,
        }
    }

    if len(save_site) == 0 or len(save_pass) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")
    else:
        try:
            with open("data.json", "r") as pass_file:
                data = json.load(pass_file)
        except FileNotFoundError:
            with open("data.json", "w") as pass_file:
                json.dump(new_data, pass_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as pass_file:
                # Saving
                json.dump(data, pass_file, indent=4)
        finally:
            input_site.delete(0, END)
            input_pass.delete(0, END)
            input_site.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, heigh=200, highlightthickness=0)
pass_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_logo)

label_site = Label(text="Website:", font=(FONT_NAME, 12, "bold"))
label_user = Label(text="Email/Username:", font=(FONT_NAME, 12, "bold"))
label_pass = Label(text="Password", font=(FONT_NAME, 12, "bold"))

input_site = Entry(width=21)
input_site.focus()
input_user = Entry(width=35)
input_user.insert(0, DEFAULT_EMAIL)
input_pass = Entry(width=21)

button_fnd = Button(text="Search", highlightthickness=0, width=14, command=search_password)
button_gen = Button(text="Generate Password", highlightthickness=0, command=generate_password)
button_add = Button(text="Add", highlightthickness=0, width=36, command=save_password)

canvas.grid(column=1, row=0)

label_site.grid(column=0, row=1)
label_user.grid(column=0, row=2)
label_pass.grid(column=0, row=3)

input_site.grid(column=1, row=1)
input_user.grid(column=1, row=2, columnspan=2)
input_pass.grid(column=1, row=3)

button_fnd.grid(column=2, row=1)
button_gen.grid(column=2, row=3)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
