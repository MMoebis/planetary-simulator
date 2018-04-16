from tkinter import *
import math
import sys

def bestaetigen(event):
    text = textfeld.get('1.0', 'end').strip()
    Compare = str(compare)
    if text == Compare:
        textfeld.insert(END, insert)


root = Tk()
root.title("PS")
root.geometry("1920x1080")

textfeld = Text(master=root)
textfeld.config(wrap='word', width="1920",
                height="1080", bg="black",
                foreground="white", insertbackground="white",
                font="Monaco")
textfeld.pack(fill="both")

root.bind('<Return>', bestaetigen)

root.mainloop()

class infinity:
	def __init__(self, xexp, yexp):
		self.__universes = []
		self.__xexp = 0
		self.__yexp = 0
		
	def addUniverse(self, universe):
		self.__universes.append(universe)
		return true
	
	def removeUniverse(self, universe):
		self.__universes.remove(universe)
		return true
	
	def getUniverse(self, i):
		return universes[i]

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

#    def v(self):
#        v = Body.addForce(((Vector().magnitude()).normalize()))*gravitation())

#        return v

    
class commands:
	
    def define(self):
		com1 = "universe"
		com2 = "rules"
		
		usrCom = input()
		
		if usrCom == com1:
			ret = universe()
			return ret
		
#		if usrCom == com2:
#			ret = rules()
#			return ret
		
        def universe(self):
			print("please insert universe data! (G, maxX, maxY)")
			inp = input()
			self.__G = int(inp)
			inp2 = input()
			self.__maxX = int(inp2)
			inp3= input()
			self.__maxY = int(inp3)
			
			return Universe(G, maxX, maxY)
		
#		def rules(self, comNumb = 1): 
			
	
	def add(self):
		com1 = "body"
		usrCom = input()
		
		if usrCom == com1:
			ret = body()
			return ret
		
		def body(self):
			print("please insert planet data! (m, r, xpos, ypos)")
			inp = input()
			self.__m = int(inp)
			inp2 = input()
			self.__r = int(inp2)
			inp3 = input()
			self.__xpos = int(inp3)
			inp4 = input()
			self.__ypos = int(inp4)
			
			return Body(m, r, xpos, ypos)
	
    def show(self):
		com1 = "animation"
		com2 = "diagram"
		com3 = "calculator"
		
		usrCom = input()
		
		if usrCom == com1:
			ret = animation()
			return ret
		
		if usrCom == com2:
			ret = diagram()
			return ret
		
		if usrCom == com3:
			ret = calculator()
			return ret
		
		def animation(self):
			
		def diagram(self):
		
		def calculator(self):
			
    def delete(self):
		com1 = "universe"
		com2 = "body"
		
		usrCom = input()
		
		if usrCom == com1:
			ret = universe()
			return ret
		
		if usrCom == com2:
			ret = body()
			return ret
		
		def universe(self):
			Universe.delBody(0)
			Infinity.removeUniverse(0)
			
		def body(self):
			
				
      
        
    
    

