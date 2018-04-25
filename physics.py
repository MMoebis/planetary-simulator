from math import sqrt
from tkinter import *
import time


class Vector2:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __add__(self, other):
        x = self.__x + other.__x
        y = self.__y + other.__y

        return Vector2(x, y)

    def __sub__(self, other):
        x = self.__x - other.__x
        y = self.__y - other.__y

        return Vector2(x, y)

    def __mul__(self, other):
        return Vector2(self.__x * other, self.__y * other)

    def __truediv__(self, other):
        return Vector2(self.__x / other, self.__y / other)

    def distance(self, other):
        a = self.__x - other.__x
        b = self.__y - other.__y
        return sqrt(a ** 2 + b ** 2)

    def normalize(self):
        d = self.magnitude()
        return Vector2(self.__x / d, self.__y / d)

    def magnitude(self):
        return sqrt(self.__x ** 2 + self.__y ** 2)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __str__(self):
        return "(" + str(self.__x) + ", " + str(self.__y) + ")"


class Body:
    def __init__(self, m, pos):
        self.__m = m
        self.__pos = pos
        self.__velocity = Vector2(0, 0)

    def add_force(self, force):
        self.__velocity += force / self.__m

    def get_pos(self):
        return self.__pos

    def get_velocity(self):
        return self.__velocity

    def get_mass(self):
        return self.__m

    def update_pos(self, delta_time):
        self.__pos += self.__velocity * delta_time


class Planet(Body):
    def __init__(self, m, pos, r, canvas, outline='white', fill='blue'):
        super().__init__(m, pos)
        self.__r = r
        self.__canvas = canvas
        self.__canvas_id = canvas.create_oval(pos.get_x() - r, pos.get_y() - r,
                                              pos.get_x() + r, pos.get_y() + r,
                                              outline=outline, fill=fill)

    def update_canvas(self):
        pos = self.get_pos()
        r = self.__r
        self.__canvas.coords(self.__canvas_id,
                             pos.get_x() - r, pos.get_y() - r,
                             pos.get_x() + r, pos.get_y() + r)


class Universe:
    def __init__(self, g):
        self.__bodies = []
        self.__g = g
        self.__current = 0

    def add_body(self, body):
        self.__bodies.append(body)

    def compute_physics(self, delta_time):
        for i in range(len(self.__bodies)):
            for j in range(i+1, len(self.__bodies)):
                body1 = self.__bodies[i]
                body2 = self.__bodies[j]
                body1.add_force(self.__compute_inter_force(body1, body2) * delta_time)
                body2.add_force(self.__compute_inter_force(body2, body1) * delta_time)
        for i in self.__bodies:
            i.update_pos(delta_time)

    def __compute_inter_force(self, body1, body2):
        mass1 = body1.get_mass()
        mass2 = body2.get_mass()
        distance = body1.get_pos().distance(body2.get_pos())
        direction = body2.get_pos() - body1.get_pos()
        return direction.normalize() * (self.__g * mass1 * mass2 / distance ** 2)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current >= len(self.__bodies):
            self.__current = 0
            raise StopIteration
        else:
            self.__current += 1
            return self.__bodies[self.__current-1]

    def __getitem__(self, item):
        return self.__bodies[item]


class Main:
    def __init__(self, g=100000, delta_time=0.01):
        self.__root = Tk()
        self.__canvas = Canvas(self.__root, width=400, height=400)
        self.__canvas.pack()
        self.__delta_time = delta_time
        self.universe = Universe(g=g)
        self.test()
        self.__canvas.pack()
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