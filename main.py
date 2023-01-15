from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


def generatePassword():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i ", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "u", "z"]
    zahlen = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    symbole = ["!", "#", "$", "%", "%", "(", ")", "*", "+ "]


    passwordLetters = [choice(letters) for l in range(randint(8, 10))]
    passwordZahlen = [choice(zahlen) for z in range(randint(2, 4))]
    passwordSymbole = [choice(symbole) for s in range(randint(2, 4))]

    passwordList = passwordLetters + passwordSymbole + passwordZahlen
    shuffle(passwordList)

    password = "".join(passwordList)
    password_entry.insert(0, password)
    pyperclip.copy(password)



def handleSavePassword():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",
                            message="Please make sure you have not left any fields blank.")
    else:
        isOk = messagebox.askokcancel(title=website,
                                       message=f"These are the details:\nEmail:{email}\nPassword:{password}\n Is it ok to save?")


    if isOk:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

email_entry.insert(0, "georgenatro@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generatePassword)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=handleSavePassword)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
