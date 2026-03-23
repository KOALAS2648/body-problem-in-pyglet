import pyglet
from pyglet import shapes

class Spaceship(shapes.Circle):
    def __init__(self, x, y, xvel, yvel, mass, radius, segments = None, color = ..., blend_src = ..., blend_dest = ..., batch = None, group = None, program = None):
        super().__init__(x, y, radius, segments, color, blend_src, blend_dest, batch, group, program)
        self.x = x
        self.y = x
        self.xvel = xvel
        self.yvel = yvel
        self.mass = mass
    def distance(self, other: object):
        return (other.x-self.x)**2 + (self.y-other.y)**2
    def get_force(self,screen,  other: object):
        force = screen.G*(self.mass*other.mass / self.distance(other))