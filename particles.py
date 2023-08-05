import pygame as pg

class Particles:
    def __init__(self, simulation, pos_x, pos_y, direction_x, direction_y, colour):
        self.particles = []
        self.simulation = simulation
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.colour = colour
    
    def emit(self):
        if self.particles:
            self.delete()
            for particle in self.particles:
                particle[0][0] += particle[2][0] * 0.5
                particle[0][1] += particle[2][1] * 0.5
                particle[1] -= 0.1
                pg.draw.circle(self.simulation.win,
                               self.colour,
                               particle[0],
                               int(particle[1]))

    def add(self):
        radius = 10
        particle = [[self.pos_x, self.pos_y], 
                    radius, 
                    [self.direction_x, self.direction_y]]
        self.particles.append(particle)

    def delete(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy

    def update(self, pos_x, pos_y, direction_x, direction_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction_x = direction_x
        self.direction_y = direction_y
