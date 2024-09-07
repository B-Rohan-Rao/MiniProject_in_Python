from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_synbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_synbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name = website_entry.get()
    email = username_entry.get()
    password_input = password_entry.get()

    if len(website_name) == 0 or len(password_input) == 0 or len(email) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure there are no empty fields")

    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the message entered:\n Email:{email}\n "
                                                                   f"Password:{password_input}\n is it ok to save:")
        if is_ok:
            with open("data.txt", "a") as a:
                a.write(f"{website_name}  |  {email}  |  {password_input}\n")
            messagebox.showinfo(title="DONE", message="DATA SAVED")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50)

# Entries
website_label = Label(text="WEBSITE:")
website_label.grid(column=1, row=1)
website_entry = Entry(width=45)
website_entry.focus()
website_entry.grid(column=2, row=1, columnspan=2)

username_label = Label(text="EMAIL/USERNAME:")
username_label.grid(column=1, row=2)
username_entry = Entry(width=45)
username_entry.insert(0, "rohanjsr098765@gmail.com")
username_entry.grid(column=2, row=2, columnspan=2)

password_label = Label(text="PASSWORD:")
password_label.grid(column=1, row=3)
password_entry = Entry(width=27)
password_entry.grid(column=2, row=3)

# Button
generate_button = Button(text="GENERATE", width=15, command=generate_password)
generate_button.grid(column=3, row=3)

add_button = Button(text="ADD", width=34, command=save_password)
add_button.grid(column=2, row=4, columnspan=3)

# Canvas
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(110, 100, image=lock_img)
canvas.grid(column=2, row=0)

window.mainloop()
