import pygame as pg
import numpy as np
from particles import Particles

G = 2
r_damping = 10

class Object:
    def __init__(self, simulation, mass, velocity, acceleration, pos, radius, colour):
        self.simulation = simulation
        self.mass = mass
        self.velocity = velocity
        self.acceleration = acceleration
        self.radius = radius
        self.pos = pos
        self.colour = colour
        self.particle_emitter = Particles(self.simulation, 
                                          self.pos[0], 
                                          self.pos[1],
                                          -self.velocity[0],
                                          -self.velocity[1],
                                          self.colour)

    def update_acceleration(self):
        temp_accel = np.array([0.0 , 0.0])
        for obj in self.simulation.simulation_objects:
            if (obj.pos == self.pos).all() == False:
                r_vector = obj.pos - self.pos
                r_magnitude = np.linalg.norm(r_vector)
                r_norm = r_vector / r_magnitude
                accel_magnitude =  G * obj.mass / (r_damping + r_magnitude) ** 2
                accel_vector = accel_magnitude * r_norm
                temp_accel += accel_vector
        
        self.acceleration = temp_accel
        return self.acceleration

    def update_movement(self):
        self.velocity += self.acceleration * self.simulation.dt / 5
        self.pos += self.velocity * self.simulation.dt / 5
        
        self.particle_emitter.update(self.pos[0],
                                     self.pos[1],
                                     -self.velocity[0],
                                     -self.velocity[1])
        
        return self.pos
    
    def draw(self):
        self.particle_emitter.emit()

        pg.draw.circle(self.simulation.win,
                       self.colour,
                       (self.pos[0], self.pos[1]),
                       self.radius)
