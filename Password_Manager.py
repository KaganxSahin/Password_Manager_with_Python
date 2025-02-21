import os.path
import random 
import pyperclip 
from tkinter import*
from tkinter.ttk import*

def low(): 
	entry.delete(0,END) 

	length= var1.get() 

	lower= "abcdefghijklmnopqrstuvwxyz"
	upper= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	digits= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
	password= "" 

	if var.get()== 1: 
		for i in range(0, length): 
			password = password + random.choice(lower) 
		return password 

	elif var.get()== 0: 
		for i in range(0, length): 
			password = password + random.choice(upper) 
		return password 

	elif var.get()== 3: 
		for i in range(0, length): 
			password = password + random.choice(digits) 
		return password 
	else: 
		print("Choose an option") 

def generate(): 
	password1= low() 
	entry.insert(10,password1) 

def copy1(): 
	random_password= entry.get() 
	pyperclip.copy(random_password) 

def checkExistence():
    if os.path.exists("info.txt"):
        pass
    else:
        file = open("info.txt",'w')
        file.close()

def appendNew():
	file = open("info.txt",'a')
	userName = entry1.get() 
	website= entry2.get()
	Random_password=entry.get()
	usrnm = "UserName: "+ userName +"\n"
	pwd = "Password: "+ Random_password +"\n"
	web = "Website: "+ website +"\n"
	file.write("---------------------------------\n")
	file.write(usrnm)
	file.write(pwd)
	file.write(web)
	file.write("---------------------------------\n")
	file.write("\n")
	file.close
	file = open("info.txt",'a')


def readPasswords():
    file = open('info.txt','r')
    content = file.read()
    file.close()
    print(content)

checkExistence()

root = Tk() 
var = IntVar() 
var1 = IntVar() 

root.title("Password Manager with Python") 

c_label = Label(root, text="Length") 
c_label.grid(row=1) 

copy_button = Button(root, text="Copy",command=copy1) 
copy_button.grid(row=0, column=2) 
generate_button = Button(root, text="Generate",command=generate) 
generate_button.grid(row=0, column=3) 

radio_low = Radiobutton(root, text="Low",variable=var,value=1) 
radio_low.grid(row=1, column=2, sticky='E') 
radio_middle = Radiobutton(root, text="Medium",variable=var,value=0) 
radio_middle.grid(row=1, column=3, sticky='E') 
radio_strong = Radiobutton(root, text="Strong",variable=var,value=3) 
radio_strong.grid(row=1, column=4, sticky='E') 
combo = Combobox(root, textvariable=var1) 

combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 
				17, 18, 19, 20, 21, 22, 23, 24, 25, 
				26, 27, 28, 29, 30, 31, 32, "Length") 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.grid(column=1,row=1) 

userName = Label(root,text="Enter username") 
userName.grid(row=2) 
entry1 = Entry(root) 
entry1.grid(row=2,column=1) 

website = Label(root,text="Enter website address") 
website.grid(row=3) 
entry2 = Entry(root) 
entry2.grid(row=3,column=1) 

Random_password = Label(root, text="Generated password") 
Random_password.grid(row=4) 
entry = Entry(root) 
entry.grid(row=4, column=1) 

save_button = Button(root, text="Save", command=appendNew) 
save_button.grid(row=2,column=2) 
show_button = Button(root, text="Show all passwords", command=readPasswords) 
show_button.grid(row=2,column=3) 

root.mainloop() 