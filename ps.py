from tkinter import *
from math import *
import sys


class Rules:
    def __init__(self, m):
        self.__m = m

    def gravitation(self, other):
        r_pp = Vector.magnitude
        G = 6, 674 * (pow(10, -11))
        F_G = G * (self.__m * other.__m) / pow(r_pp, 2)

        return F_G


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
        self._po_xs = xpos
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


define = "def"
adding = "add"
delete = "delete"
comUniverse = " universe"
comBody = " body"
show = "show"
space = " "
strSpace = space.strip()

text = ""
ret = "\n"
retCount = 1.0
i = 0

List = []
intNumber = 0

defError = "Commands missing! Available commands: -universe"
strDefError = defError.strip()
addError = "Commands missing! Available commands: -body"
strAddError = addError.strip()
showError = "Commands missing! Available commands: -animation, -diagram"
strShowError = showError.strip()
delError = "Commands missing! Available commands: -body, -universe"
strDelError = delError.strip()
genError = "No such commands available! For more help type 'help'"
strGenError = genError.strip()
heavyError = "System crashed"
strHeavyError = heavyError.strip()

succes = "Data was succesfully entered"
strSucces = succes.strip()

def disable():
    textfeld.config(state=DISABLED)
    return True

def enable():
    textfeld.config(state=NORMAL)
    return True

def getInput():
    global text
    text = textfeld.get(retCount, 'end').strip()
    print(text)
    if text != strDefError and text != strAddError and text != strShowError and text != strDelError and text != strGenError and text != strSpace:
        return text
    else:
        return True

def getNumbInput():
    global retCount
    retCount += 1.0
    global text
    global i
    global intNumber
    global List
    i += 1
    print(i)
    text = textfeld.get(retCount, 'end')
    intNumber = int(text)
    List.append(intNumber)

    return True

def errors():
    global text
    global retCount
    text = getInput()
    if text == define:
        textfeld.insert(END, defError+ret)
        retCount += 1.0
        return True
    elif text == adding:
        textfeld.insert(END, addError+ret)
        retCount += 1.0
        return True
    elif text == show:
        retCount += 1.0
        textfeld.insert(END, showError+ret)
        return True
    elif text == delete:
        retCount += 1.0
        textfeld.insert(END, delError+ret)
        return True
    else:
        return True


def commands():
    global retCount
    global i
    print(i)
    if text == define + comUniverse:
        defRequest = "Please insert universe data! (G, maxX, maxY)\n"
        retCount += 1
        textfeld.insert(END, defRequest)
        del List[:]
        i = 1

        if i == 4:
            Universe(List[0], List[1], List[2])
            textfeld.insert(END, succes + ret)
            retCount += 1.0
            i = 0
            return True

    elif text == adding + comBody:
        addRequest = "Please insert body data! (m, r, xpos, ypos)\n"
        textfeld.insert(END, addRequest)
        del List[:]
        i = 1

        if i == 5:
            retCount += 1.0
            Body(List[0], List[1], List[2], List[3])
            textfeld.insert(END, succes + ret)
            i = 0
            return True
    else:
        return False

def test(event):
    retCount = 2.0
    textfeld.insert(retCount, "test")

#	number = int(input1)
def passing():
    pass

def submit(event):
    global retCount
    print(retCount)
    err = errors()
    if err == True:
        if i != 0:
            getNumbInput()
        else:
            com = commands()
            retCount += 1
            if com == False:
                textfeld.insert(END, genError+ret)
                retCount +=1.0

    else:
        textfeld.insert(END, heavyError+ret)
        retCount +=1.0


root = Tk()
root.title("PS")
root.geometry("600x400")
menu = Menu()
root.config(menu=menu)
file = Menu(menu)
# file.add_command(label="Exit", command=self.client_exit)
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
root.bind('<Return>', submit)

root.mainloop()

# def v(self):
#        v = Body.addForce(((Vector().magnitude()).normalize()))*gravitation())

#        return v