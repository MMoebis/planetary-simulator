from tkinter import *
from physics import *
from math import *
import tkinter.filedialog as fd
import tkinter.colorchooser as cs
import sys



class Animation:
    def __init__(self, master, delta_time, g):
        self.__max_x = 0
        self.__max_y = 0

        self.__line_count = 1.0

        self.__coordinate_count = 0

        self.__point_mark = False
        self.__point_mark_x = 0
        self.__point_mark_y = 0

        self._neg_scale = 0.8
        self.__pos_scale = 1.2

        self.__scale_count = 0

        self.__scale = 1

        #self.__canvas_pos_x_scroll_region = self.__max_x
        #self.__canvas_pos_y_scroll_region = self.__max_y
        #self.__canvas_neg_x_scroll_region = -self.__max_x
        #self.__canvas_neg_y_scroll_region = -self.__max_y

        self.__planet_names = []
        self.__x_coordinates = []
        self.__y_coordinates = []
        self.__m_List = []
        self.__s_List = []

        self.__delta_time = delta_time
        self.__g = g
        self.__master = master
        self.universe = Universe(self.__g)

        self.__canvas_frame = Frame(self.__master, height=600, width=800)
        self.__canvas_frame.grid(row=0, rowspan=2, column=1)

        self.__canvas = Canvas(self.__canvas_frame, height=569, width=680, bg='black',
                               scrollregion=(-100000, -100000, 100000, 100000))

        self.__mark_line0 = self.__canvas.create_line(0, 0, 0, 0, fill='black')
        self.__mark_line1 = self.__canvas.create_line(0, 0, 0, 0, fill='black')
        self.__mark_line2 = self.__canvas.create_line(0, 0, 0, 0, fill='black')
        self.__mark_line3 = self.__canvas.create_line(0, 0, 0, 0, fill='black')

        self.__canvas_y_scroll = Scrollbar(self.__canvas_frame, command=self.__canvas.yview, orient=VERTICAL)
        self.__canvas_y_scroll.pack(side=RIGHT, fill=Y)

        self.__canvas_x_scroll = Scrollbar(self.__canvas_frame, command=self.__canvas.xview, orient=HORIZONTAL)
        self.__canvas_x_scroll.pack(side=BOTTOM, fill=X)

        self.__canvas.config(yscrollcommand=self.__canvas_y_scroll.set, xscrollcommand=self.__canvas_x_scroll.set)
        self.__canvas.pack(side=LEFT, expand=True, fill=BOTH)

        self.__button_frame = Frame(self.__master, bg='black', width=800)
        self.__button_frame.grid(row=2, column=1)

        self.__start_button = Button(self.__button_frame, text="Start", command=self.start_animation)
        self.__start_button.pack(side=LEFT)

        self.__reset_button = Button(self.__button_frame, text="Reset", command=self.reset_animation)
        self.__reset_button.pack(side=LEFT)

        self.__pos_scale_button = Button(self.__button_frame, text="Zoom in", command=self.pos_item_scale)
        self.__pos_scale_button.pack(side=LEFT)

        self.__neg_scale_button = Button(self.__button_frame, text="Zoom out", command=self.neg_item_scale)
        self.__neg_scale_button.pack(side=LEFT)

        self.__master.title("PS")

        self.__menu = Menu()
        self.__master.config(menu=self.__menu)

        self.__file = Menu(self.__menu, tearoff=0)
        self.__edit = Menu(self.__menu, tearoff=0)
        self.__background = Menu(self.__menu, tearoff=0)
        self.__new = Menu(self.__file, tearoff=0)
        self.__popup = Menu(self.__canvas,tearoff=0)

        self.__menu.add_cascade(label="File", menu=self.__file)
        self.__menu.add_cascade(label="Edit", menu=self.__edit)

        self.__file.add_cascade(label="New", menu=self.__new)
        self.__file.add_command(label="Save...", command=self.save_file)
        self.__file.add_command(label="Save as...", command=self.save_file)
        self.__file.add_command(label="Exit", command=self.exit)
        self.__popup.add_command(label="Add Body...", command=self.add_body)

        self.__edit.add_cascade(label="Background", menu=self.__background)

        self.__background.add_command(label="Animation...", command=self.edit_bg_color)
        self.__background.add_command(label="Console...", command=self.edit_bg_color)
        self.__background.add_command(label="Edit-Field...", command=self.edit_bg_color)

        self.__new.add_command(label="Universe...", command=self.define_universe)
        self.__new.add_command(label="Body...", command=self.add_body)

        self.__canvas2 = Canvas(self.__master, width=200, height=765, bg='grey')
        self.__canvas2.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.__legend_frame = Frame(self.__master, width=300, height=300)
        self.__legend_frame.grid(row=0, column=2, sticky="nsew")

        self.legend_canvas = Canvas(self.__legend_frame)

        self.__planet_label = Label(self.__legend_frame, text="Name", font=('bold', 15))
        self.__planet_label.grid(row=0, column=0, padx=16)

        self.__m_label = Label(self.__legend_frame, text="Mass (kg)", font=('bold', 15))
        self.__m_label.grid(row=0, column=1, padx=16)

        self.__r_label = Label(self.__legend_frame, text="Radius (m)", font=('bold', 15))
        self.__r_label.grid(row=0, column=2, padx=16)

        self.__color_label = Label(self.__legend_frame, text="Color", font=('bold', 15))
        self.__color_label.grid(row=0, column=3, padx=16)

        self.__canvas4 = Canvas(self.__master, height=300, width=300, bg='#D8D8D8')
        self.__canvas4.grid(row=1, column=2, sticky="nsew", rowspan=2)

        self.__text_frame = Frame(self.__master, height=10, width=138)
        self.__text_frame.grid(column=1, row=3, columnspan=3, sticky="nsew")

        self.__text_y_scroll = Scrollbar(self.__text_frame)
        self.__text_y_scroll.pack(side=RIGHT, fill=Y)

        self.__textfield = Text(self.__text_frame, height=10, width=138, bg='#424242',
                                foreground='white', insertbackground='white', font=('Monaco', 10),
                                yscrollcommand=self.__text_y_scroll.set)

        self.__textfield.pack(side=LEFT, fill=BOTH, expand="Yes")

        self.__text_y_scroll.config(command=self.__textfield.yview)

        self.__canvas.bind('<ButtonPress-3>', self.get_mouse_coordinates)
        self.__canvas.bind('<B3-Motion>', self.canvas_drag)
        self.__canvas.bind('<Button-1>', self.mark_coordinate)
        self.__canvas.bind('<Button-2>', self.options)

        self.__master.grid_rowconfigure(0, weight=2)
        self.__master.grid_rowconfigure(1, weight=2)
        self.__master.grid_rowconfigure(2, weight=1)
        self.__master.grid_columnconfigure(1, weight=10)
        self.__master.grid_columnconfigure(2, weight=1)

        self.__callback = True

        self.test()

    def test(self):
        self.universe.add_body(Planet(1e18, Vector2(250, 250), "t1", 10, self.__scale, self.__canvas, fill='orange'))
        self.universe.add_body(Planet(1e18, Vector2(450, 450), "t2", 10, self.__scale, self.__canvas, fill='blue'))
        self.universe.add_body(Planet(1e18, Vector2(850, 650), "t3", 10, self.__scale, self.__canvas, fill='yellow'))
        self.universe.add_body(Planet(1e18, Vector2(1050, 850), "t4", 10, self.__scale, self.__canvas, fill='lightblue'))
        self.universe.add_body(Planet(1e18, Vector2(600, 250), "t5", 8, self.__scale, self.__canvas, fill='green'))
        self.universe.add_body(Planet(1e18, Vector2(750, 300), "t6", 6, self.__scale, self.__canvas, fill='red'))
        self.universe.add_body(Planet(1e18, Vector2(950, 500), "t7", 5, self.__scale, self.__canvas, fill="black"))
        self.universe.add_body(Planet(1e18, Vector2(250, 750), "t8", 10, self.__scale, self.__canvas, fill='lightgreen'))
        self.universe[0].add_force(Vector2(0, 20))
        self.universe[1].add_force(Vector2(0, -30))

    def update(self):
        while self.__callback == True:
            self.__canvas.update()
            for i in self.universe:
                i.set_scale(self.__scale)
                i.update_canvas()

            self.universe.compute_physics(self.__delta_time)
            time.sleep(self.__delta_time)
            #self.transitional_collision()

    def update_canvas_scrollregion(self):
        transitional = self.universe.maximum_coordinates()

        self.__max_x = transitional[0]
        self.__max_y = transitional[1]

        print(self.__max_x)

        if self.__max_x < 0:
            self.__max_x = -self.__max_x

        if self.__max_y < 0:
            self.__max_y = -self.__max_y

        print(self.__max_x)

        self.__canvas.config(scrollregion=(-self.__max_x, -self.__max_y, self.__max_x, self.__max_y))

    def get_mouse_coordinates(self, event):
        self.__canvas.scan_mark(event.x, event.y)

    def canvas_drag(self, event):
        self.__canvas.scan_dragto(event.x, event.y, gain=2)

    def neg_item_scale(self):
        self.__scale_count -= 1
        if self.__scale_count > 0:
            self.__scale = self.__pos_scale ** self.__scale_count

        if self.__scale_count < 0:
            self.__scale = self._neg_scale ** (self.__scale_count * (-1))

        self.__canvas.scale("all", 0, 0, self._neg_scale, self._neg_scale)

    def pos_item_scale(self):
        self.__scale_count += 1
        if self.__scale_count > 0:
            self.__scale = self.__pos_scale ** self.__scale_count

        if self.__scale_count < 0:
            self.__scale = self._neg_scale ** (self.__scale_count * (-1))

        self.__canvas.scale("all", 0, 0, self.__pos_scale, self.__pos_scale)

    def mark_coordinate(self, event):
        self.__canvas.delete(self.__mark_line0, self.__mark_line1, self.__mark_line2, self.__mark_line3)
        self.__point_mark = True
        self.__point_mark_x = event.x
        self.__point_mark_y = event.y
        self.__mark_line0 = self.__canvas.create_line(event.x+15, event.y, event.x+5, event.y, fill='white')
        self.__mark_line1 = self.__canvas.create_line(event.x, event.y+15, event.x, event.y+5, fill='white')
        self.__mark_line2 = self.__canvas.create_line(event.x-15, event.y, event.x-5, event.y, fill='white')
        self.__mark_line3 = self.__canvas.create_line(event.x, event.y-15, event.x, event.y-5, fill='white')

        self.__textfield.insert(self.__line_count, "X: " + str(event.x) + " Y: " + str(event.y))
        self.__line_count += 1

        print(self.__line_count)

    def options(self, event):
        if self.__point_mark == True:
            self.__popup.post(self.__point_mark_x, self.__point_mark_y)

    def start_animation(self):
        self.__callback = True
        self.__start_button.configure(text="Stop", command=self.stop_animation)
        self.__canvas.after(0, self.update)
        #self.__canvas.after(0, self.update_canvas_scrollregion)

    def stop_animation(self):
        self.__start_button.configure(text="Start", command=self.start_animation)
        self.__callback = False
        self.__canvas.after(0, self.update)
        #self.__canvas.after(0, self.update_canvas_scrollregion)

    def collision(self):
        print("error 1")
        for e in self.universe:
            print("error 2")
            for f in self.universe:
                print("error 3")
                planet1 = e.get_pos() * e.get_scale()
                planet2 = f.get_pos() * f.get_scale()
                x = planet1.get_x() - planet2.get_x()
                y = planet1.get_y() - planet2.get_y()
                distance = sqrt(x**2 + y**2)

                if e.get_name() != f.get_name():
                    print("error 4")
                    if distance == e.get_r() * e.get_scale() + f.get_r() * f.get_scale():
                        print("error 5")
                        if e.get_r() < f.get_r():
                            print("error 6")
                            self.universe.delete_item(planet1)
                        if f.get_r() < e.get_r():
                            print("error 7")
                            self.universe.delete_item(planet2)

    def transitional_collision(self):
        for e in self.universe:
            for f in self.universe:
                if e.get_name() != f.get_name() and e.get_pos() == f.get_pos():
                    self.universe.delete_item(f)

    def reset_animation(self):
        self.__canvas.delete("all")
        self.__start_button.configure(text="Start", command=self.start_animation)
        self.__callback = False
        self.universe = Universe(self.__g)
        for c in range(self.__coordinate_count):
            self.rN = self.__planet_names[c]
            self.rX = self.__x_coordinates[c]
            self.rY = self.__y_coordinates[c]
            self.rM = self.__m_List[c]
            self.rS = self.__s_List[c]

            self.universe.add_body(Planet(self.M, Vector2(self.X, self.Y), self.rN, self.S, self.__canvas, fill='orange'))

    def submit(self):
        print("submit")

    def exit(self):
        sys.exit(0)

    def save_file(self):
        self.__save = fd.askopenfilename()
        print(self.__save)

    def edit_bg_color(self):
        self.__color = cs.askcolor(color='black', title="choose a color")
        print(self.__color)

    def define_universe(self):
        self.master1 = Tk()
        self.master1.title("define a universe")
        self.e1 = Entry(self.master1)
        self.e2 = Entry(self.master1)
        self.submit1 = Button(self.master1, text="Submit", command=self.submit)

        self.l1 = Label(self.master1, text="Name")
        self.l2 = Label(self.master1, text="G \n(gravitational constant)")

        self.e1.grid(row=0, column=1, padx=5, pady=5)
        self.e2.grid(row=1, column=1, padx=5, pady=5)
        self.submit1.grid(row=2, columnspan=2)
        self.l1.grid(row=0, column=0, padx=5, pady=5)
        self.l2.grid(row=1, column=0, padx=5, pady=5)

    def add_body(self):
        self.master2 = Tk()
        self.master2.title("add a body")

        self.e3 = Entry(self.master2)
        self.e4 = Entry(self.master2)
        self.e5 = Entry(self.master2)
        self.e6 = Entry(self.master2)
        self.e7 = Entry(self.master2)

        self.l3 = Label(self.master2, text="Name")
        self.l4 = Label(self.master2, text="X \n (position in coordinate system)")
        self.l5 = Label(self.master2, text="Y \n (position in coordinate system)")
        self.l6 = Label(self.master2, text="m \n (mass)")
        self.l7 = Label(self.master2, text="radius")
        self.submit2 = Button(self.master2, text="submit", command=self.add_body_submit)

        self.e3.grid(row=0, column=1, padx=2.5, pady=2.5)
        self.e4.grid(row=1, column=1, padx=2.5, pady=2.5)
        self.e5.grid(row=2, column=1, padx=2.5, pady=2.5)
        self.e6.grid(row=3, column=1, padx=2.5, pady=2.5)
        self.e7.grid(row=4, column=1, padx=2.5, pady=2.5)
        self.l3.grid(row=0, column=0, padx=2.5, pady=2.5)
        self.l4.grid(row=1, column=0, padx=2.5, pady=2.5)
        self.l5.grid(row=2, column=0, padx=2.5, pady=2.5)
        self.l6.grid(row=3, column=0, padx=2.5, pady=2.5)
        self.l7.grid(row=4, column=0, padx=2.5, pady=2.5)
        self.submit2.grid(row=5, columnspan=2)

        if self.__point_mark == True:
            self.e4.insert(0, self.__point_mark_x)
            self.e5.insert(0, self.__point_mark_y)

    def add_body_submit(self):
        print(self.__scale_count)

        row = 1
        column = 0

        self.N = self.e3.get().strip()

        self.x = self.e4.get().strip()
        self.X = int(self.x)

        self.y = self.e5.get().strip()
        self.Y = int(self.y)

        self.m = self.e6.get().strip()
        self.M = int(self.m)

        self.s = self.e7.get().strip()
        self.S = int(self.s)

        self.adding = self.universe.add_body(Planet(self.M, Vector2(self.X, self.Y), self.N, self.S, self.__scale, self.__canvas, fill='orange'))

        print(self.adding)

        a = self.universe.get_planet_info()
        print(a)

        self.__planet_names.append(self.N)
        self.__coordinate_count += 1
        self.__x_coordinates.append(self.X)
        self.__coordinate_count += 1
        self.__y_coordinates.append(self.Y)
        self.__coordinate_count += 1
        self.__m_List.append(self.M)
        self.__coordinate_count += 1
        self.__s_List.append(self.S)
        self.__coordinate_count += 1

        for p in range(len(self.__planet_names)):
            Label(self.__legend_frame, text=self.__planet_names[p]).grid(row=row, column=column)
            column += 1
            Label(self.__legend_frame, text=self.__m_List[p]).grid(row=row, column=column)
            column += 1
            Label(self.__legend_frame, text=self.__s_List[p]).grid(row=row, column=column)
            column = 0
            row += 1
            #Label(self.__legend_frame, text=self.__)

        #self.universe[0].add_force(Vector2(0, 20))
        #self.universe[1].add_force(Vector2(0, -30))

        self.__textfield.insert(self.__line_count, "The body " + "'" + self.N + "'" + " was sucessfully added to Universe!")
        self.__line_count += 1

        self.__point_mark = False

        self.master2.destroy()


if __name__ == '__main__':
    root = Tk()
    Animation(root, 0.01, 0.0000000000067408)
    root.mainloop()