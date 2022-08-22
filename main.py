from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip



# Password Generator Project:
# Mit dieser Funktion generieren wir das Passwort,
# indem wir eine Variable aus allen Buchstaben, Zahlen und Symbolen erstellen.
# Dann machen wir Variablen, die eine zufällige Auswahl aus den obigen Arrays treffen.

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




# Password speichern:
# Mit dieser Funktion stellen wir sicher,
# dass die Website, E-Mail und das Passwort, die wir geschrieben haben,
# in einer neuen Datei namens data.txt gespeichert werden

def speichern():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",
                            message=" Bitte stellen Sie sicher dass Sie keine Felder leer gelassen haben.")
    else:
        isOk = messagebox.askokcancel(title=website,
                                       message=f"Diese sind die Details:\nEmail:{email}\nPassword:{password}\n Ist es ok , zu speichern ?")


    if isOk:
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
generate_password_button = Button(text="Generate Password", command=generatePassword)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=speichern)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
