from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_information():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) > 0 and len(password) > 0 and len(email) > 0:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details that you entered: "
                                                              f"\nEmail: {email} \nPassword: {password} "
                                                              f"\nIs it okay to save this information?")

        if is_ok:
            with open(file="data.txt", mode="a") as file:
                file.write(f"\n{website} | {email} | {password}")

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
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Email/Username
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.insert(0, "jhecker2001@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

# Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)

# Generate Password
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)

# Add Entry
add_button = Button(text="Add", width=30, command=save_information)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
