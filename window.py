from tkinter import *
import tkinter.filedialog as fd
import tkinter.colorchooser as cs
import sys
from physics import *

class Window():
    def __init__(self, master):
        self.__master = master

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

        # frame1 = Frame(self.__root, width=800, height=600)

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
        self.__root.grid_rowconfigure(1, weight=2)
        self.__root.grid_rowconfigure(2, weight=1)
        #    self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_columnconfigure(1, weight=10)
        self.__root.grid_columnconfigure(2, weight=1)

        self.__delta_time = delta_time
        self.universe = Universe(g=g)
        self.test()
        self.__root.after(0, self.update)

        self.__root.mainloop()
