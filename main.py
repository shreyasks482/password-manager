from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import pandas
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&']
word = ""
x = random.choices(letters, weights=None, k=10)
for n in x:
    word += n
y = random.choices(numbers, weights=None, k=4)
for m in y:
    word += m
z = random.choices(symbols, weights=None, k=3)
for l in z:
    word += l

password = ''.join(random.sample(word, len(word)))
pyperclip.copy(password)


def generate():
    passinput.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = nameinput.get().title()
    mails = mailinput.get()
    pas = passinput.get()
    info = {
        web: {
            "email": mails,
            "password": pas
        }
    }

    if len(web) == 0 or len(pas) == 0:
        messagebox.showwarning(title="Oops!", message="Hey don't leave the boxes empty!!")

    else:
        ## You can either save data in a txt file or csv file or json file
        # is_ok = messagebox.askokcancel(title=web, message=f"The details you have entered are:\nYour website: {web}\nYour password: {pas}")
        # if is_ok:
        # data=pandas.read_csv("data.csv")
        # with open("data.txt", "a") as fp:
        #     fp.write(f"{web} | {mails} | {pas}\n")
        try:
            with open("data.json", "r") as fp:
                data = json.load(fp)
        except FileNotFoundError:
            with open("data.json", "w") as fp:
                json.dump(info, fp, indent=4)
        else:
            data.update(info)

            with open("data.json", "w") as fp:
                json.dump(data, fp, indent=4)
        finally:
            nameinput.delete(0, END)
            passinput.delete(0, END)


# -------------------------------SEARCH----------------------------------#

def search():
    website = nameinput.get().title()
    try:
        with open("data.json") as fp:
            data = json.load(fp)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data file found")

    else:
        if website in data:
            email = data[website]["email"]
            paswrd = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {paswrd}")
        else:
            messagebox.showerror(title="Oops!", message=f"Given {website} website does not exist")
            passinput.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
title = window.title("Password Manager")
window.config(padx=60, pady=60)
window.minsize(width=450, height=350)
canvas = Canvas(width=200, height=200, highlightbackground="green")
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=1, column=2)

name = Label(text="Website: ", height=2)
name.grid(row=2, column=1)

mail = Label(text="Email/username: ", height=2)
mail.grid(row=3, column=1)

passwor = Label(text="Password: ", height=2)
passwor.grid(row=4, column=1)

nameinput = Entry(width=33)
nameinput.grid(row=2, column=2)

search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=2, column=3)

mailinput = Entry(width=51)
mailinput.grid(row=3, column=2, columnspan=2)

passinput = Entry(width=33)
passinput.grid(row=4, column=2)

gbutton = Button(text="Generate Password", width=14, command=generate)
gbutton.grid(row=4, column=3)

addbutton = Button(text="Add", width=43, command=save)
addbutton.grid(row=5, column=2, columnspan=2)

nameinput.focus()
mailinput.insert(0, "Your default Email")

window.mainloop()



