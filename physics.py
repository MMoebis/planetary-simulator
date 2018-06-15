from math import sqrt
from tkinter import *
import time

# Klasse fuer Vektoren (Der Name "Vector2" wurde gewaehlt, da es bereits eine Klasse Vector in tkinter gibt)


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

    # Distanz zweier Planeten wird berechnet

    def distance(self, other):
        a = self.__x - other.__x
        b = self.__y - other.__y
        return sqrt(a ** 2 + b ** 2)

    def normalize(self):
        d = self.magnitude()
        return Vector2(self.__x / d, self.__y / d)

    # Umwandlung eines Positionsvektors in einen Richtungsvektor

    def magnitude(self):
        return sqrt(self.__x ** 2 + self.__y ** 2)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __str__(self):
        return "(" + str(self.__x) + ", " + str(self.__y) + ")"


class Body:
    def __init__(self, m, pos, name):
        self.__name = name
        self.__m = m
        self.__pos = pos
        self.__velocity = Vector2(0, 0)

    def get_name(self):
        return self.__name

    # Kraft wirkt aus einer best. Richtung auf den Koerper

    def add_force(self, force):
        self.__velocity += force / self.__m

    def get_pos(self):
        return self.__pos

    def get_X(self):
        return self.get_pos().get_x()

    def get_Y(self):
        return self.get_pos().get_y()

    def get_velocity(self):
        return self.__velocity

    def set_velocity(self, velocity):
        self.__velocity = velocity

    def get_mass(self):
        return self.__m

    def update_pos(self, delta_time):
        self.__pos += self.__velocity * delta_time


class Planet(Body):
    def __init__(self, m, pos, name, r, scale, canvas, color, outline='white'):
        super().__init__(m, pos, name)
        self.__color = color
        self.__r = r
        self.__scale = scale
        self.__canvas = canvas
        self.__name = name
        self.__last_pos = Vector2(0, 0)
        self.__canvas_id = canvas.create_oval(pos.get_x() - r * self.__scale, pos.get_y() - r * self.__scale,
                                              pos.get_x() + r * self.__scale, pos.get_y() + r * self.__scale,
                                              outline=outline, fill=self.__color)

    def set_scale(self, scale):
        self.__scale = scale

    def get_scale(self):
        return self.__scale

    def get_name(self):
        return self.__name

    def update_canvas(self):
        pos = self.get_pos()
        r = self.__r
        self.__canvas.coords(self.__canvas_id,
                             pos.get_x() * self.__scale - r * self.__scale, pos.get_y() * self.__scale - r * self.__scale,
                             pos.get_x() * self.__scale + r * self.__scale, pos.get_y() * self.__scale + r * self.__scale)

    def get_r(self):
        return self.__r

    def get_canvas_id(self):
        return self.__canvas_id

    def get_last_pos(self):
        return self.__last_pos

    def set_last_pos(self, pos):
        self.__last_pos = pos

    def get_color(self):
        return self.__color


class Universe:
    def __init__(self, g):
        self.__bodies = []
        self.__g = g
        self.__current = 0
        self.__ret_list = []
        self.__body_velocity = []

    def add_body(self, body):
        self.__bodies.append(body)

    # physikalische Interaktion zweier Koerper wird berechnet

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
        #norm = direction.normalize()
        ret = direction.normalize() * (self.__g * mass1 * mass2 / distance ** 2)
        #last = self.__g * mass1 * mass2 / distance ** 2
        #dist = body1.get_pos().distance(body2.get_pos())
        #print(ret, direction, dist, norm, last)
        return ret

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

    def maximum_coordinates(self):
        max_values = []
        max_x = 0
        max_y = 0
        x_list = []
        y_list = []

        for j in range(len(self.__bodies)):
            planet = self.__getitem__(j)
            x = planet.get_X()
            x_list.append(x)
            y = planet.get_Y()
            y_list.append(y)
        for k in range(len(x_list)-1):
            if x_list[k+1] > x_list[k] and x_list[k+1] > max_x:
                max_x = x_list[k+1]
        for l in range(len(y_list)-1):
            if y_list[l+1] > y_list[l] and y_list[l+1] > max_y:
                max_y = y_list[l+1]

        max_values.append(max_x)
        max_values.append(max_y)

        return max_values

    def get_planet_info(self):
        info_list = []
        name_list = []
        mass_list = []
        radius_list =[]

        for p in range(len(self.__bodies)):
            planet = self.__getitem__(p)
            name_list.append(planet.get_name())
            mass_list.append(planet.get_mass())
            radius_list.append(planet.get_r())

        return info_list.append(name_list), info_list.append(mass_list), info_list.append(radius_list)

    def delete_item(self, item):
        self.__bodies.remove(item)

    def collision(self):
        ret_list = []
        ret_list.append(False)
        if len(self.__bodies) > 1:
            for i in range(len(self.__bodies)):
                for j in range(i + 1, len(self.__bodies)):
                    body1 = self.__bodies[i]
                    body2 = self.__bodies[j]
                    body1_pos = body1.get_pos()
                    body2_pos = body2.get_pos()
                    distance = body1_pos.distance(body2_pos)
                    body1_scale = body1.get_scale()
                    body2_scale = body2.get_scale()
                    r1 = body1.get_r() * body1_scale
                    r2 = body2.get_r() * body2_scale
                    body1_canvas_id = body1.get_canvas_id()
                    body2_canvas_id = body2.get_canvas_id()

                    if distance <= r1 + r2:
                        if r1 > r2:
                            ret_list[0] = True
                            if r2 * 10000 < r1:
                                ret_list.append(False)
                                self.__bodies.remove(body2)
                                ret_list.append(body2_canvas_id)
                                return ret_list
                            else:
                                ret_list.append(True)
                                ret_list.append(body1)
                                ret_list.append(body2)
                                return ret_list
                        if r1 < r2:
                            ret_list[0] = True
                            if r1 * 10000 < r2:
                                ret_list.append(False)
                                self.__bodies.remove(body1)
                                ret_list.append(body1_canvas_id)
                                return ret_list
                            else:
                                ret_list.append(True)
                                ret_list.append(body1)
                                ret_list.append(body2)
                                return ret_list
                        if r1 == r2:
                            ret_list[0] = True
                            ret_list.append(True)
                            ret_list.append(body1)
                            ret_list.append(body2)
                            return ret_list
                    else:
                        return ret_list
        else:
            return ret_list

    def get_bodies(self):
        return len(self.__bodies)
