import os.path
import random 
import pyperclip 
from tkinter import *
from tkinter.ttk import *

def checkExistence():
    if not os.path.exists("info.txt"):
        with open("info.txt", 'w') as file:
            pass

def low(): 
    entry.delete(0, END)
    length = var1.get()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""
    
    if var.get() == 1: 
        password = "".join(random.choice(lower) for _ in range(length))
    elif var.get() == 0: 
        password = "".join(random.choice(upper) for _ in range(length))
    elif var.get() == 3: 
        password = "".join(random.choice(digits) for _ in range(length))
    else: 
        print("Choose an option")
    
    return password 

def generate(): 
    password1 = low()
    entry.insert(10, password1)

def copy1(): 
    pyperclip.copy(entry.get())

def appendNew():
    with open("info.txt", 'a') as file:
        userName = entry1.get()
        website = entry2.get()
        random_password = entry.get()
        file.write("---------------------------------\n")
        file.write(f"UserName: {userName}\n")
        file.write(f"Password: {random_password}\n")
        file.write(f"Website: {website}\n")
        file.write("---------------------------------\n\n")

def readPasswords():
    with open('info.txt', 'r') as file:
        print(file.read())

checkExistence()

root = Tk()
root.title("Password Manager with Python")

var = IntVar()
var1 = IntVar()

Label(root, text="Length").grid(row=1)
Label(root, text="Enter username").grid(row=2)
Label(root, text="Enter website address").grid(row=3)
Label(root, text="Generated password").grid(row=4)

entry1 = Entry(root)
entry1.grid(row=2, column=1)
entry2 = Entry(root)
entry2.grid(row=3, column=1)
entry = Entry(root)
entry.grid(row=4, column=1)

Button(root, text="Copy", command=copy1).grid(row=0, column=2)
Button(root, text="Generate", command=generate).grid(row=0, column=3)
Button(root, text="Save", command=appendNew).grid(row=2, column=2)
Button(root, text="Show all passwords", command=readPasswords).grid(row=2, column=3)

Radiobutton(root, text="Low", variable=var, value=1).grid(row=1, column=2, sticky='E')
Radiobutton(root, text="Medium", variable=var, value=0).grid(row=1, column=3, sticky='E')
Radiobutton(root, text="Strong", variable=var, value=3).grid(row=1, column=4, sticky='E')

combo = Combobox(root, textvariable=var1)
combo['values'] = tuple(range(8, 33)) + ("Length",)
combo.current(0)
combo.grid(column=1, row=1)

root.mainloop()
