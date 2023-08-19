import pygame as pg
from vector import Vector
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from math import pi, cos, tan, atan2

class Camera:
    def __init__(self, sim, FOV, pos, cam_angle_x, cam_angle_y):
        self.sim = sim
        self.FOV = FOV
        self.pos = pos
        self.cam_angle_x = cam_angle_x
        self.cam_angle_y = cam_angle_y

    # Rotates camera accordingly to keys pressed
    def check_rotation(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            self.pos = self.pos.subtract(Vector(self.sim.dt / 1000, 0, 0))

        if keys[pg.K_d]:
            self.pos = self.pos.add(Vector(self.sim.dt / 1000, 0, 0))
        
        if keys[pg.K_w]:
            self.pos = self.pos.subtract(Vector(0, self.sim.dt / 1000, 0))
        
        if keys[pg.K_s]:
            self.pos = self.pos.add(Vector(0, self.sim.dt / 1000, 0))
        
        if keys[pg.K_q]:
            self.pos = self.pos.add(Vector(0, 0, self.sim.dt / 1000))
        
        if keys[pg.K_e]:
            self.pos = self.pos.subtract(Vector(0, 0, self.sim.dt / 1000))
        
        if keys[pg.K_LEFT]:
            self.cam_angle_x -= self.sim.dt / 1000
            self.cam_angle_x = (self.cam_angle_x % (2 * pi))
            if self.cam_angle_x > pi:
                self.cam_angle_x -= 2 * pi
        
        if keys[pg.K_RIGHT]:
            self.cam_angle_x += self.sim.dt / 1000
            self.cam_angle_x = (self.cam_angle_x % (2 * pi))
            if self.cam_angle_x > pi:
                self.cam_angle_x -= 2 * pi

        if keys[pg.K_UP]:
            self.cam_angle_y -= self.sim.dt / 1000
            self.cam_angle_y = (self.cam_angle_y % (2 * pi))
            if self.cam_angle_y > pi:
                self.cam_angle_y -= 2 * pi
        
        if keys[pg.K_DOWN]:
            self.cam_angle_y += self.sim.dt / 1000
            self.cam_angle_y = (self.cam_angle_y % (2 * pi))
            if self.cam_angle_y > pi:
                self.cam_angle_y -= 2 * pi

    # Calculates how an object will look on camera screen given its coordinates.
    def projected(self, obj):
        k = 10

        dx = obj.pos.x - self.pos.x
        dy = obj.pos.y - self.pos.y
        dz = obj.pos.z - self.pos.z

        obj_angle_xz = atan2(dx, dz)
        obj_angle_yz = atan2(dy, dz)

        r = abs(dz / (cos(obj_angle_xz) * cos(obj_angle_yz)))

        hx = SCREEN_WIDTH / (2 * tan(self.FOV / 2))
        hy = SCREEN_HEIGHT / (2 * tan(self.FOV / 2))

        x_proj = hx * tan(obj_angle_xz - self.cam_angle_x) + SCREEN_WIDTH / 2
        y_proj = hy * tan(obj_angle_yz - self.cam_angle_y) + SCREEN_HEIGHT / 2

        size = k / r

        return (x_proj, y_proj, size)
    

