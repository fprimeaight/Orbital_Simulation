import pygame as pg
import sys
import numpy as np
from objects import Object

class Simulation:
    def __init__(self):
        pg.init()
        self.win = pg.display.set_mode((800, 600))
        self.clock = pg.time.Clock()
        self.simulation_objects = []
        self.dt = 1
        self.scrolling = False
        self.mouse_origin = pg.mouse.get_pos()
        self.trail_surface = pg.Surface((800, 600))

        self.PARTICLE_EVENT = pg.USEREVENT + 1
        pg.time.set_timer(self.PARTICLE_EVENT, 20)

        obj1 = Object(self,
                      mass=100,
                      velocity=np.array([-2.1, 0.0]),
                      acceleration=np.array([0.0, 0.0]),
                      pos=np.array([400.0, 100.0]),
                      radius=5.0,
                      colour='blue')

        obj2 = Object(self,
                      mass=500.0,
                      velocity=np.array([-0.2, 0.3]),
                      acceleration=np.array([0.0, 0.0]),
                      pos=np.array([400.0, 300.0]),
                      radius=20.0,
                      colour='red')
        
        obj3 = Object(self,
                      mass=230.0,
                      velocity=np.array([-1.0, 0.0]),
                      acceleration=np.array([0.0, 0.0]),
                      pos=np.array([500.0, 30.0]),
                      radius=17.0,
                      colour='green')
        
        self.simulation_objects.append(obj1)
        self.simulation_objects.append(obj2)
        self.simulation_objects.append(obj3)
        
    def draw(self):
        self.win.fill('black')
        for obj in self.simulation_objects:
            obj.draw()

    def update(self):
        for obj in self.simulation_objects:
            obj.update_acceleration()
            obj.update_movement()
            self.dt = self.clock.tick(1000)
            pg.display.set_caption(f'{self.clock.get_fps():.1f}')

        if self.scrolling == True:
            origin_x, origin_y = self.mouse_origin
            mouse_x, mouse_y = pg.mouse.get_pos()
            shift_x = mouse_x - origin_x
            shift_y = mouse_y - origin_y

            shift_vector = np.array([shift_x, shift_y])

            for obj in self.simulation_objects:
                obj.pos += shift_vector

                for particle in obj.particle_emitter.particles:
                    particle[0][0] += shift_x
                    particle[0][1] += shift_y

            self.mouse_origin = pg.mouse.get_pos()
        
        pg.display.flip()

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            
            if event.type == self.PARTICLE_EVENT:
                for obj in self.simulation_objects:
                    obj.particle_emitter.add()

            if event.type == pg.MOUSEBUTTONDOWN:
                self.scrolling = True
                self.mouse_origin = pg.mouse.get_pos()
                
            if event.type == pg.MOUSEBUTTONUP:
                self.scrolling = False
                
    def run(self):
        while True:
            self.check_event()
            self.draw()
            self.update()


if __name__ == '__main__':
    s = Simulation()
    s.run()