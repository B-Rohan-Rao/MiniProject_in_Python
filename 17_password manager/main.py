import json
from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip


# ---------------------------- WRITE TO JSON ------------------------------- #
def write_to_json(data):
    """Writes data to the JSON file."""
    with open("data.json", "w") as w:
        json.dump(data, w, indent=4)


def read_from_json():
    """Reads data from the JSON file."""
    try:
        with open("data.json", "r") as r:
            data = json.load(r)
        return data
    except FileNotFoundError:
        return {}


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.delete(0, END)  # Clear the password field before inserting
    password_entry.insert(0, password)
    pyperclip.copy(password)  # Copy the generated password to the clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name = website_entry.get().upper()
    email = username_entry.get()
    password_input = password_entry.get()
    new_data = {
        website_name: {
            "email": email,
            "password": password_input,
        }
    }

    if len(website_name) == 0 or len(password_input) == 0 or len(email) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure there are no empty fields")
    else:
        data = read_from_json()
        data.update(new_data)
        write_to_json(data)
        messagebox.showinfo(title="DONE", message="DATA SAVED")
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website_name = website_entry.get().upper()
    data = read_from_json()

    if website_name in data:
        email = data[website_name]['email']
        password = data[website_name]['password']
        messagebox.showinfo(title=website_name, message=f"Email: {email}\nPassword: {password}")
    else:
        messagebox.showinfo(title="OOPS", message="No details for the website exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50)

# Labels
website_label = Label(text="WEBSITE:")
website_label.grid(column=1, row=1)
username_label = Label(text="EMAIL/USERNAME:")
username_label.grid(column=1, row=2)
password_label = Label(text="PASSWORD:")
password_label.grid(column=1, row=3)

# Entries
website_entry = Entry(width=30)
website_entry.grid(column=2, row=1)
website_entry.focus()

username_entry = Entry(width=45)
username_entry.grid(column=2, row=2, columnspan=2)
username_entry.insert(0, "rohanjsr098765@gmail.com")

password_entry = Entry(width=30)
password_entry.grid(column=2, row=3)

# Buttons
search_button = Button(text="SEARCH", width=15, command=search_password)  # Correct function binding
search_button.grid(column=3, row=1)

generate_button = Button(text="GENERATE", width=15, command=generate_password)
generate_button.grid(column=3, row=3)

add_button = Button(text="ADD", width=34, command=save_password)
add_button.grid(column=2, row=4, columnspan=3)

# Canvas for logo
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(110, 100, image=lock_img)
canvas.grid(column=2, row=0)

window.mainloop()
