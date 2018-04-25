from tkinter import *
import sys
import math

def submit():
	print("submit")

root = Tk()
root.title("PS")
#root.geometry("600x400")
menu = Menu()
root.config(menu=menu)
file = Menu(menu)
new = Menu(file)
# file.add_command(label="Exit", command=self.client_exit)
menu.add_cascade(label="File", menu=file)
file.add_cascade(label="New", menu=new)
file.add_command(label="Exit")
file.add_command(label="Save...")
file.add_command(label="Save as...")

new.add_command(label="Universe")
new.add_command(label="Body")

canvas = Canvas(root, width=300, height=300, bg='black')
canvas.grid(rowspan=20, columnspan=3, column=3, padx=5)

e0 = Entry(root)
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)

rLabel = Label(root, text = "Define a Universe!")
e0Label = Label(root, text = "Name")
e1Label = Label(root, text = "G")
e2Label = Label(root, text = "maxX(m)")
e3Label = Label(root, text = "maxY(m)")

submit = Button(root, text = "Submit", command=submit)

e0.grid(row=2, column = 1, pady = 2, padx = 2)
e1.grid(row=3, column = 1, pady = 2, padx = 2)
e2.grid(row=4, column = 1, pady = 2, padx = 2)
e3.grid(row=5, column = 1, pady = 2, padx = 2)

rLabel.grid(row=1, column = 1, pady = 2)
e0Label.grid(row=2, column = 0)
e1Label.grid(row=3, column = 0)
e2Label.grid(row=4, column = 0)
e3Label.grid(row=5, column = 0)


submit.grid(row=6, column = 1, pady = 2)

root.mainloop()	