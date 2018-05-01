from tkinter import *
import sys

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("BYSS")
        self.pack(fill=BOTH, expand=1)
        #quitButton = Button(self, text="Exit", command=self.client_exit)
        #quitButton.place(x=0, y=0)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        edit = Menu(menu)
        edit.add_command(label="Undo")
        menu.add_cascade(label="Edit", menu=edit)

    def client_exit(self):
        sys.exit(0)

root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()

class Koerper:
    import math
    r = 0
    m = 0
    d = r * 2
    u = 2 * math.pi * r
    def koerper(self, r, m):
        self.r = r
        self.m = m

class Planet(Koerper):
    Zentralgestirn = ""

class Trabant(Koerper):
    ZentralKoerper = ""