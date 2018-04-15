from tkinter import *
import math
import sys

def bestaetigen(event):
    text = textfeld.get('1.0', 'end').strip()
    Compare = str(compare)
    if text == Compare:
        textfeld.insert(END, insert)


root = Tk()
root.title("Test")
root.geometry("1920x1080")

textfeld = Text(master=root)
textfeld.config(wrap='word', width="1920",
                height="1080", bg="black",
                foreground="white", insertbackground="white",
                font="Monaco")
textfeld.pack(fill="both")

root.bind('<Return>', bestaetigen)

root.mainloop()

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

        return Vector(x,y)

    def __sub__(self, other):
        x = self.__x - other.__x
        y = self.__y - other.__y

        return Vector(x,y)
        
    def magnitude(self, other):
        a = self.__x - other.__x
        b = self.__y - other.__y
        c = sqrt(pow(a, 2)+pow(b, 2))

        return c

    def normalize(self):
        d = self.magnitude()
        Vector(self.__x/d, self.__y/d)

        return Vector(x,y)

class Rules:
    def __init__(self, m):
        self.__m = m
        

    def gravitation(self, other):
        r_pp = Vector.magnitude() 
        G = 6,674*(pow(10, -11))
        F_G = G * (self.__m * other.__m)/pow(r_pp, 2)

        return F_G

    def v(self):
 #       v = Body.addForce(((Vector().magnitude()).normalize()))*F_G)

        return v

    
#class commands:
#    def define(self):
#        def 
        
        
        
        
    
    
    
