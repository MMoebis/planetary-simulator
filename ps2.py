from tkinter import *

def submit():
	print("submit")

root = Tk()
root.title("PS")
#root.geometry("600x400")
menu = Menu()
root.config(menu=menu)
file = Menu(menu)
# file.add_command(label="Exit", command=self.client_exit)
menu.add_cascade(label="File", menu=file)
edit = Menu(menu)
edit.add_command(label="Undo")
menu.add_cascade(label="Edit", menu=edit)

canvas = Canvas(root, width=200, height=200)
canvas.pack()

e0 = Entry(root)
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)

rLabel = Label(root, text="Define a Universe!")
e0Label = Label(root, text="Name")
e1Label = Label(root, text="G")
e2Label = Label(root, text="maxX(m)")
e3Label = Label(root, text="maxY(m)")


submit = Button(root, text="Submit", command=submit)

e0.grid(row=2, column=1, pady=2, padx=2)
e1.grid(row=3, column=1, pady=2, padx=2)
e2.grid(row=4, column=1, pady=2, padx=2)
e3.grid(row=5, column=1, pady=2, padx=2)

rLabel.grid(row=1, column=1, pady=2)
e0Label.grid(row=2, column=0)
e1Label.grid(row=3, column=0)
e2Label.grid(row=4, column=0)
e3Label.grid(row=5, column=0)


submit.grid(row=6, column=1, pady=2)

root.mainloop()