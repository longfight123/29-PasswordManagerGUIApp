"""

This script allows the user to keep track of passwords
to websites and generate random passwords. The users
information is stored in a JSON file. The user can also
search for passwords for a specific website.

This script requires that 'tkinter', 'pyperclip' be installed within the Python
environment you are running this script in.

"""

import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- Search Functionality -------------------
def search_json():
    """Searches the JSON file for the password
    for the website that the user wants.
    """
    website = website_entry.get()
    try:
        with open('./password.json', 'r') as password_file:
            data = json.load(password_file)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No Data File Found.')
    else:
        if website in data.keys():
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Website: {website}\nEmail: {email}\nPassword: {password}')
        else:
            messagebox.showerror(title='Sorry', message='No details for the website exists. Check spelling.')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generates a random password and stores it
    in the users clipboard"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list_symbols = [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list_numbers = [random.choice(numbers) for char in range(random.randint(2, 4))]

    password_list = password_list_numbers+password_list_letters+password_list_symbols
    random.shuffle(password_list)

    password = ''.join(password_list)
    pyperclip.copy(password)
    password_entry.insert(index=0, string=password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    """Adds a new JSON object containing the website, email, and password
    """
    email = email_entry.get()
    password = password_entry.get()
    website = website_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }
    if len(email) == 0 or len(password) == 0 or len(website) ==0:
        messagebox.showerror(title='Ooops', message='Please don\'t leave any fields empty!')
    else:
        try:
            with open('./password.json', 'r') as password_file:
                data = json.load(password_file)
                data.update(new_data)
        except FileNotFoundError:
            with open('./password.json', 'w') as password_file:
                json.dump(new_data, password_file, indent=4)
        else:
            with open('./password.json', 'w') as password_file:
                json.dump(data, password_file, indent=4)
        website_entry.delete(first=0, last=len(website))
        password_entry.delete(first=0, last=len(password))
        messagebox.showinfo(title='Ok', message='Password was added to database.')
# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
photo_image = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo_image)
canvas.grid(row=1, column=2)

#Labels
website_label = tkinter.Label(text='Website:')
website_label.grid(row=2, column=1)
email_label = tkinter.Label(text='Email/Username:')
email_label.grid(row=3, column=1)
password_label = tkinter.Label(text='Password')
password_label.grid(row=4, column=1)
#Entries
website_entry = tkinter.Entry(width=32)
website_entry.grid(row=2, column=2)
website_entry.focus()
email_entry = tkinter.Entry(width=51)
email_entry.insert(index=0, string='youremail@gmail.com')
email_entry.grid(row=3, column=2, columnspan=2)
password_entry = tkinter.Entry(width=32)
password_entry.grid(row=4, column=2)
#Buttons
generate_pw_button = tkinter.Button(text='Generate Password', command=generate_password)
generate_pw_button.grid(row=4, column=3)
add_button = tkinter.Button(text='Add', width=44, command=add_password)
add_button.grid(row=5, column=2, columnspan=2)
search_button = tkinter.Button(text='Search', width=14, command=search_json)
search_button.grid(row=2, column=3)

window.mainloop()