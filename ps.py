from tkinter import *
import tkinter.filedialog as fd
import tkinter.colorchooser as cs
import sys
from physics import *



# textfield/canvas = 6,21

class Main:
    def __init__(self, g=0.0000000000667408, delta_time=0.0001):
        self.__root = Tk()
        self.__root.title("PS")

        self.__menu = Menu()
        self.__root.config(menu=self.__menu)

        self.__file = Menu(self.__menu, tearoff=0)
        self.__edit = Menu(self.__menu, tearoff=0)
        self.__background = Menu(self.__menu, tearoff=0)
        self.__new = Menu(self.__file, tearoff=0)

        self.__menu.add_cascade(label="File", menu=self.__file)
        self.__menu.add_cascade(label="Edit", menu=self.__edit)

        self.__file.add_cascade(label="New", menu=self.__new)
        self.__file.add_command(label="Save...", command=self.save_file)
        self.__file.add_command(label="Save as...", command=self.save_file)
        self.__file.add_command(label="Exit", command=self.exit_window)

        self.__edit.add_cascade(label="Background", menu=self.__background)

        self.__background.add_command(label="Animation...", command=self.edit_bg_color)
        self.__background.add_command(label="Console...", command=self.edit_bg_color)
        self.__background.add_command(label="Edit-Field...", command=self.edit_bg_color)

        self.__new.add_command(label="Universe...", command=self.define_universe)
        self.__new.add_command(label="Body...", command=self.add_body)

        #frame1 = Frame(self.__root, width=800, height=600)

        self.__canvas = Canvas(self.__root, width=800, height=600, bg='#424242')
        self.__canvas.grid(rowspan=2, column=1, sticky="nsew")

        self.__canvas2 = Canvas(self.__root, width=200, height=765, bg='grey')
        self.__canvas2.grid(row=0, column=0, rowspan=3, sticky="nsew")

        self.__canvas3 = Canvas(self.__root, width=300, height=300, bg='#BDBDBD')
        self.__canvas3.grid(row=0, column=2, sticky="nsew")

        self.__canvas4 = Canvas(self.__root, height=300, width=300, bg='#D8D8D8')
        self.__canvas4.grid(row=1, column=2, sticky="nsew")

        self.__textfield = Text(self.__root, height=10, width=138, bg='black',
                                foreground='white', insertbackground='white', font=('Monaco', 10))
        self.__textfield.grid(column=1, row=2, columnspan=2, sticky="nsew")
        self.__root.grid_rowconfigure(0, weight=2)
        self.__root.grid_rowconfigure(1,weight=2)
        self.__root.grid_rowconfigure(2, weight=1)
    #    self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_columnconfigure(1, weight=10)
        self.__root.grid_columnconfigure(2, weight=1)

        self.__delta_time = delta_time
        self.universe = Universe(g=g)
        self.test()
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
        self.universe.add_body(Planet(5000000000000000000, Vector2(250, 250), 10, self.__canvas, fill='orange'))
        self.universe.add_body(Planet(5000000000000000000, Vector2(450, 450), 10, self.__canvas, fill='blue'))
        self.universe.add_body(Planet(5000000000000000000, Vector2(850, 650), 10, self.__canvas, fill='yellow'))
        self.universe.add_body(Planet(5000000000000000000, Vector2(1050, 850), 10, self.__canvas, fill='lightblue'))
        self.universe.add_body(Planet(3000000000000000000, Vector2(600, 250), 8, self.__canvas, fill='green'))
        self.universe.add_body(Planet(1000000000000000000, Vector2(750, 300), 6, self.__canvas, fill='red'))
        self.universe.add_body(Planet(1000000000000000000, Vector2(950, 500), 5, self.__canvas, fill="black"))
        self.universe.add_body(Planet(5, Vector2(250, 750), 10, self.__canvas, fill='lightgreen'))
        self.universe[0].add_force(Vector2(0, 20))
        self.universe[1].add_force(Vector2(0, -30))

    def submit(self):
        print("submit")

    def exit_window(self):
        sys.exit(0)

    def save_file(self):
        save = fd.askopenfilename()
        print(save)

    def edit_bg_color(self):
        color = cs.askcolor(color='black', title="choose a color")
        print(color)

    def define_universe(self):
        uni = Tk()
        uni.title("define a universe")
        e1 = Entry(uni)
        e2 = Entry(uni)
        submit1 = Button(uni, text="Submit", command=self.submit)

        l1 = Label(uni, text="Name")
        l2 = Label(uni, text="G \n(gravitational constant)")

        e1.grid(row=0, column=1, padx=5, pady=5)
        e2.grid(row=1, column=1, padx=5, pady=5)
        submit1.grid(row=2, columnspan=2)
        l1.grid(row=0, column=0, padx=5, pady=5)
        l2.grid(row=1, column=0, padx=5, pady=5)

    def add_body(self):
        self.__body = Tk()
        self.__body.title("add a body")

        self.__e3 = Entry(self.__body)
        self.__e4 = Entry(self.__body)
        self.__e5 = Entry(self.__body)
        self.__e6 = Entry(self.__body)

        self.l3 = Label(self.__body, text="Name")
        self.__l4 = Label(self.__body, text="X \n (position in coordinate system)")
        self.__l5 = Label(self.__body, text="Y \n (position in coordinate system)")
        self.__l6 = Label(self.__body, text="m \n (mass)")

        self.__submit2 = Button(self.__body, text="submit", command=self.add_body_submit)

        self.__e3.grid(row=0, column=1, padx=2.5, pady=2.5)
        self.__e4.grid(row=1, column=1, padx=2.5, pady=2.5)
        self.__e5.grid(row=2, column=1, padx=2.5, pady=2.5)
        self.__e6.grid(row=3, column=1, padx=2.5, pady=2.5)
        self.__l3.grid(row=0, column=0, padx=2.5, pady=2.5)
        self.__l4.grid(row=1, column=0, padx=2.5, pady=2.5)
        self.__l5.grid(row=2, column=0, padx=2.5, pady=2.5)
        self.__l6.grid(row=3, column=0, padx=2.5, pady=2.5)
        self.__submit2.grid(row=4, columnspan=2)

    def add_body_submit(self):
        x = self.__e4.get('1.0', 'end').strip()
        self.__X = int(x)

        y = self.__e5.get('1.0', 'end').strip()
        self.__Y = int(y)

        m = self.__e6.get('1.0', 'end').strip()
        self.__M = int(m)
        self.universe.add_body(Planet(self.__M, Vector2(self.__X, self.__Y), 20, self.__canvas, fill='darkred'))


if __name__ == '__main__':
    Main()