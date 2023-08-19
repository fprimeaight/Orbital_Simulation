import pygame as pg
import sys
from object import Object
from vector import Vector
from camera import Camera
from settings import FOV, SCREEN_WIDTH, SCREEN_HEIGHT

class Simulation:
    def __init__(self):
        pg.init()
        self.win = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        self.obj = []
        self.dt = 1
        self.light = Vector(30, 50, 50)
        self.camera = Camera(sim=self,
                             FOV=FOV,
                             pos=Vector(),
                             cam_angle_x=0,
                             cam_angle_y=0)
        
        s1 = Object(sim=self,
                    mass=0,
                    r=3,
                    pos=Vector(1, 0, 3),
                    col=(14, 209,69),
                    vel=Vector(),
                    acc=Vector(),
                    id=0)
        
        s2 = Object(sim=self,
                    mass=0,
                    r=3,
                    pos=Vector(0, 0, 3),
                    col=(63, 72, 204),
                    vel=Vector(),
                    acc=Vector(),
                    id=1)
        
        s3 = Object(sim=self,
                    mass=0,
                    r=3,
                    pos=Vector(0, -1, 3),
                    col=(255, 0, 0),
                    vel=Vector(),
                    acc=Vector(),
                    id=2)
        
        self.obj.append(s1)
        self.obj.append(s2)
        self.obj.append(s3)
        self.z_sort()

    def z_sort(self):
        for i in range(len(self.obj) - 1):
            for j in range(len(self.obj) - 1):
                if self.obj[j].pos.z < self.obj[j + 1].pos.z:
                    t = self.obj[j]
                    self.obj[j] = self.obj[j + 1]
                    self.obj[j + 1] = t

    def draw(self):
        self.win.fill((0, 0, 0))
        for obj in self.obj:
            obj.draw(self.light)
    
    def update(self):
        self.z_sort()
        for obj in self.obj:
            obj.update()
        
        self.dt = self.clock.tick(1000)
        pg.display.set_caption(f'''FPS: {self.clock.get_fps():.1f} 
                               CamAngleX: {self.camera.cam_angle_x:.1f} 
                               CamAngleY: {self.camera.cam_angle_y:.1f}
                               CamPos: {self.camera.pos}''')
        pg.display.flip()

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        self.camera.check_rotation()
        
    def run(self):
        while True:
            self.check_event()
            self.draw()
            self.update()

if __name__ == '__main__':
    s = Simulation()
    s.run()
