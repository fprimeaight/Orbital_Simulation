import pygame as pg
from vector import Vector
from math import sqrt
from settings import G, R_DAMPING

class Object:
    def __init__(self, sim, mass, r, pos, col, vel, acc, id):
        self.sim = sim
        self.mass = mass
        self.r = r
        self.pos = pos
        self.col = col
        self.vel = vel
        self.acc = acc
        self.id = id

    def update(self):
        a = Vector()
        for obj in self.sim.obj:
            if obj.id != self.id and obj.mass > 0 and self.mass > 0:
                r_v = obj.pos.subtract(self.pos)
                r_m = r_v.magnitude()
                r_v.norm()
                a_m = G * obj.mass / (R_DAMPING + r_m) ** 2
                a_v = r_v.scalar(a_m)
                a = a.add(a_v)
        
        self.acc = a
        self.vel = self.vel.add(self.acc.scalar(self.sim.dt / 1000))
        self.pos = self.pos.add(self.vel.scalar(self.sim.dt / 1000))

    def draw(self, light_vector):
        light_vector.norm()
        bg_light = 0
        res = 10
        x_proj, y_proj, size = self.sim.camera.projected(self)

        for i in range(-res * self.r, res * self.r + 1):
            y = i / res
            for j in range(-res * self.r, res * self.r + 1):
                x = j / res

                if x ** 2 + y ** 2 <= self.r ** 2:
                    v = Vector(x, y, -sqrt(self.r ** 2 - x ** 2 - y ** 2))
                    v.norm()
                    b = v.dot(light_vector) ** 2 + bg_light
                    if b > 1:
                        col = (self.col[0], self.col[1], self.col[2])
                    else:
                        col = (b * self.col[0], 
                               b * self.col[1], 
                               b * self.col[2])
        
                    pg.draw.rect(surface=self.sim.win,
                                 color=col,
                                 rect=pg.Rect(x * size + x_proj,
                                             y * size + y_proj,
                                             int(max(1, size)),
                                             int(max(1, size))))         
