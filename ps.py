from tkinter import *
import tkinter.filedialog as fd
import tkinter.colorchooser as cs
import sys
from physics import *
from syntax import *


# textfield/canvas = 6,21

def save_file():
    save = fd.askopenfilename()
    print(save)


def edit_bg_color():
    color = cs.askcolor(color='black', title="choose a color")
    print(color)


def define_universe():
    uni = Tk()
    uni.title("define a universe")
    e1 = Entry(uni)
    e2 = Entry(uni)
    submit1 = Button(uni, text="Submit", command=submit)

    l1 = Label(uni, text="Name")
    l2 = Label(uni, text="G \n(gravitational constant)")

    e1.grid(row=0, column=1, padx=5, pady=5)
    e2.grid(row=1, column=1, padx=5, pady=5)
    submit1.grid(row=2, column=1)
    l1.grid(row=0, column=0, padx=5, pady=5)
    l2.grid(row=1, column=0, padx=5, pady=5)


def add_body():
    body = Tk()
    body.title("add a body")

    e3 = Entry(body)
    e4 = Entry(body)
    e5 = Entry(body)
    e6 = Entry(body)

    l3 = Label(body, text="Name")
    l4 = Label(body, text="X \n (position in coordinate system)")
    l5 = Label(body, text="Y \n (position in coordinate system)")
    l6 = Label(body, text="m \n (mass)")

    e3.grid(row=0, column=1, padx=2.5, pady=2.5)
    e4.grid(row=1, column=1, padx=2.5, pady=2.5)
    e5.grid(row=2, column=1, padx=2.5, pady=2.5)
    e6.grid(row=3, column=1, padx=2.5, pady=2.5)
    l3.grid(row=0, column=0, padx=2.5, pady=2.5)
    l4.grid(row=1, column=0, padx=2.5, pady=2.5)
    l5.grid(row=2, column=0, padx=2.5, pady=2.5)
    l6.grid(row=3, column=0, padx=2.5, pady=2.5)


def submit():
    print("submit")


def exit_window():
    sys.exit(0)


root = Tk()
root.title("PS")
menu = Menu()
root.config(menu=menu)

file = Menu(menu, tearoff=0)
edit = Menu(menu, tearoff=0)
background = Menu(menu, tearoff=0)
new = Menu(file, tearoff=0)

menu.add_cascade(label="File", menu=file)
menu.add_cascade(label="Edit", menu=edit)

file.add_cascade(label="New", menu=new)
file.add_command(label="Save...", command=save_file)
file.add_command(label="Save as...", command=save_file)
file.add_command(label="Exit", command=exit_window)

edit.add_cascade(label="Background", menu=background)

background.add_command(label="Animation...", command=edit_bg_color)
background.add_command(label="Console...", command=edit_bg_color)
background.add_command(label="Edit-Field...", command=edit_bg_color)

new.add_command(label="Universe...", command=define_universe)
new.add_command(label="Body...", command=add_body)

#canvas = Canvas(root, width=800, height=600, bg='#424242')
#canvas.grid(rowspan=200, column=1, columnspan=102)

canvas2 = Canvas(root, width=200, height=765, bg='grey')
canvas2.grid(row=0, column=0, rowspan=211)

canvas3 = Canvas(root, width=300, height=300, bg='#BDBDBD')
canvas3.grid(row=0, column=103, rowspan=50)

canvas4 = Canvas(root, height=300, width=300, bg='#D8D8D8')
canvas4.grid(row=51, column=103, rowspan=50)

textfield = Text(root, height=10, width=138, bg='black',
                 foreground='white', insertbackground='white', font=('Monaco', 10))
textfield.grid(row=201, rowspan=11, column=1, columnspan=1000)




class Main:
    def __init__(self, g=100000, delta_time=0.01):
        global root
#        self.__root = Tk()
        self.__canvas = Canvas(root, width=800, height=600, bg='#424242')
        self.__canvas.grid(rowspan=200, column=1, columnspan=102)
#        self.__canvas.pack()
        self.__delta_time = delta_time
        self.universe = Universe(g=g)
        self.test()
#       self.__canvas.pack()
        self.__root.after(0, self.update)
        self.__root.mainloop()

    def update(self):
        while True:
            self.__canvas.update()
            for i in self.universe:
                i.update_canvas()
            self.universe.compute_physics(self.__delta_time)
            time.sleep(self.__delta_time)

    def test(self):
        self.universe.add_body(Planet(1.5, Vector2(100, 100), 10, self.__canvas, fill='blue'))
        self.universe.add_body(Planet(1, Vector2(200, 200), 8, self.__canvas, fill='green'))
        self.universe.add_body(Planet(0.5, Vector2(150, 300), 6, self.__canvas, fill='red'))
        self.universe[0].add_force(Vector2(0, 20))
        self.universe[1].add_force(Vector2(0, -30))

if __name__ == '__main__':
    Main()

root.mainloop()