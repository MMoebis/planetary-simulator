from tkinter import *
from math import *
import sys

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
    global text
    global i
    global intNumber
    global List
    i += 1
    text = textfeld.get(retCount, 'end').strip()
    print(text)
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
        defRequest = "Please insert universe data! (G, maxX, maxY)"
        retCount += 1
        textfeld.insert(END, defRequest+ret)
        del List[:]
        i = 1
        print(i)

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

#	number = int(input1)

def submit(event):
    global retCount
    print(retCount)
    err = errors()
    if err == True:
        if i != 0:
            getNumbInput()
            retCount += 1
        else:
            com = commands()
            retCount += 1
            if com == False:
                textfeld.insert(END, genError+ret)
                retCount +=1.0

    else:
        textfeld.insert(END, heavyError+ret)
        retCount +=1.0