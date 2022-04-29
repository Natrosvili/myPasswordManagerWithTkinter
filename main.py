from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# Password Generator Project:
def generate_password():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i ", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "u", "z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    symbols = ["!", "#", "$", "%", "%", "(", ")", "*", "+ "]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# Password speichern:
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",
                            message=" Bitte stellen Sie sicher dass Sie keine Felder leer gelassen haben.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Diese sind die Details:\nEmail:{email}\nPassword:{password}\n Ist es ok , zu speichern ?")

    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# Set Up:
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Labels:
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries:
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

# Hier können Sie ihr Email schreiben
email_entry.insert(0, "georgenatro@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons:
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
