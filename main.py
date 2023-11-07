from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- SEARCH TERMS ------------------------------------- #


def find_password():
    website = website_entry.get().lower()
    try:
        with open(file="data.json", mode="r") as file:
            data = json.load(file)
            if website in data:
                messagebox.showinfo(title=f"{website}", message=f"Here is your data: "
                                                                 f"\nemail: {data[website]['email']} "
                                                                 f"\npassword: {data[website]['password']}")
            else:
                messagebox.showerror(title="Website not found", message="No details for the website exists.")
    except FileNotFoundError:
        messagebox.showerror(title="Missing data.json", message="No Data File Found")
    finally:
        website_entry.delete(0, END)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    letter_list = [choice(LETTERS) for _ in range(randint(8, 10))]
    number_list = [choice(NUMBERS) for _ in range(randint(2, 4))]
    symbol_list = [choice(SYMBOLS) for _ in range(randint(2, 4))]

    password_list = letter_list + number_list + symbol_list

    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_information():
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) > 0 and len(password) > 0 and len(email) > 0:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details that you entered: "
                                                              f"\nEmail: {email} \nPassword: {password} "
                                                              f"\nIs it okay to save this information?")

        if is_ok:
            try:
                with open(file="data.json", mode="r") as file:
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data

            with open(file="data.json", mode="w") as file:
                json.dump(data, file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showerror(title="Blank Entry", message="Do not leave a field blank.")


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

# Search Button
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1)

# Email/Username
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=39)
email_entry.insert(0, "---@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

# Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Generate Password
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

# Add Entry
add_button = Button(text="Add", width=30, command=save_information)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
