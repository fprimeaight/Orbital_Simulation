from math import sqrt

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def add(self, v):
        return Vector(self.x + v.x,
                      self.y + v.y,
                      self.z + v.z)
    
    def subtract(self, v):
        return Vector(self.x - v.x,
                      self.y - v.y,
                      self.z - v.z)
            
    def scalar(self, k):
        x = k * self.x
        y = k * self.y
        z = k * self.z

        return Vector(x, y, z) 
    
    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def norm(self):
        m = sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        self.x = self.x / m
        self.y = self.y / m
        self.z = self.z / m
        
    def dot(self, v):
        d = self.x * v.x + self.y * v.y + self.z * v.z
        if d < 0:
            return -d
        else:
            return 0
        
    def __str__(self):
        return f'[{self.x:.1f}, {self.y:.1f}, {self.z:.1f}]'