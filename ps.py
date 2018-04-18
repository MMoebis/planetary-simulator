from tkinter import *
from math import *
import sys

def getInput():
    text = textfeld.get('1.0', 'end').strip()
    return text

def commands(event):
    define = "def"
    adding = "add"
    defUniverse = "def universe"
#	universe = "universe"
    addBody = "add body"
    delete = "del"
    show = "show"
    text = getInput()
		
	
    if text == define:
       defError = "commands missing!\navailable commands: universe\n"
       textfeld.insert(END, defError)

    if text == adding:
        addError = "commands missing!\navailable commands: body\n"
        textfeld.insert(END, addError)

    if text == defUniverse:
        defRequest = "Please insert universe data! (G, maxX, maxY)\n"
        textfeld.insert(END, defRequest)
        defG = getNumbInput()
        defMaxX = getNumbInput()
        defMaxY = getNumbInput()

        universe = Universe(defG, defMaxX, defMaxY)
        Infinity.addUniverse(universe)

    if text == addBody:
        addRequest = "Please insert body data! (m, r, xpos, ypos)\n"
        textfeld.insert(END, addRequest)
        addM = getNumbInput()
        addR = getNumbInput()
        addXpos = getNumbInput()
        addYpos = getNumbInput()

        body = Body(addM, addR, addXpos, addYpos)
        Universe.addBody(body)

def test(event):
    print("test")

def getNumbInput():
	input1 = textfeld.get('1.0', 'end').strip()
	number = int(input1)
	
	return number
	
root = Tk()
root.title("PS")
root.geometry("200x200")
menu = Menu()
root.config(menu=menu)
file = Menu(menu)
#file.add_command(label="Exit", command=self.client_exit)
menu.add_cascade(label="File", menu=file)
edit = Menu(menu)
edit.add_command(label="Undo")
menu.add_cascade(label="Edit", menu=edit)

textfeld = Text(master=root)
textfeld.config(wrap='word', width="1920",
                height="1080", bg="black",
                foreground="white", insertbackground="white",
                font="Monaco")
textfeld.pack(fill="both")


root.bind('<Return>', commands)

root.mainloop()


class Infinity:
    def __init__(self):
        self.__universes = []

    def addUniverse(self, universe):
        self.__universes.append(universe)
        return True

    def removeUniverse(self, universe):
        self.__universes.remove(universe)
        return True

    def getUniverse(self, i):
        return self.__universes[i]

class Body:
    def __init__(self, m, r, xpos, ypos):
        self.__m = m
        self.__r = r
        self.__xpos = xpos
        self.__ypos = ypos

    def addForce(self, x, y):
        vec = Vector(x, y)

        return vec


class Universe:
    def __init__(self, G, maxX, maxY):
        self.__bodys = []
        self.__G = G
        self.__maxX = maxX
        self.__maxY = maxY

    def addBody(self, body):
        self.__bodys.append(body)

    def delBody(self, i):
        del self.__bodys[i]

    def getBody(self, i):
        return self.__bodys[i]


class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __add__(self, other):
        x = self.__x + other.__x
        y = self.__y + other.__y

        return Vector(x, y)

    def __sub__(self, other):
        x = self.__x - other.__x
        y = self.__y - other.__y

        return Vector(x, y)

    def magnitude(self, other):
        a = self.__x - other.__x
        b = self.__y - other.__y
        c = sqrt(pow(a, 2) + pow(b, 2))

        return c

    def normalize(self):
        d = self.magnitude(self)
        vd = Vector(self.__x / d, self.__y / d)

        return vd


class Rules:
    def __init__(self, m):
        self.__m = m

    def gravitation(self, other):
        r_pp = Vector.magnitude
        G = 6, 674 * (pow(10, -11))
        F_G = G * (self.__m * other.__m) / pow(r_pp, 2)

        return F_G


# def v(self):
#        v = Body.addForce(((Vector().magnitude()).normalize()))*gravitation())

#        return v
