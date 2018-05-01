from tkinter import *

root =Tk()
root.geometry("400x400")

canvas = Canvas(root, width=200, height=400, bg='blue')
canvas2 = Canvas(root, width=200, height=400, bg='red')

canvas.grid(row=0, column=0, sticky="nsew")
canvas2.grid(row=0, column=1, sticky="nsew")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)


root.mainloop()