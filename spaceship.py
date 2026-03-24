import pyglet
from pyglet import shapes
from pyglet.gl import GL_SRC_ALPHA, GL_ONE
import math
class Spaceship(shapes.Circle):
    def __init__(self, startx, starty, xvel, yvel, mass, radius, segments = None, color =(255,255,255),blend_src = GL_SRC_ALPHA, blend_dest = GL_ONE, batch = None, group = None, program = None):
        super().__init__(startx, starty, radius, segments, color, blend_src, blend_dest, batch, group, program)
        self.x = startx
        self.y = starty
        self.velx = xvel
        self.vely = yvel
        self.mass = mass
    def distance(self, other: object):
        return (other.x-self.x)**2 + (self.y-other.y)**2
    def get_force(self,screen,  other: object):
        force = screen.G*(self.mass*other.mass / self.distance(other))
        return force
    def move(self, screen, other):
        otherx, othery = other.x, other.y
        deltax = self.x-otherx
        deltay = othery-self.y
        angle = math.atan2(deltay, deltax)
        force = self.get_force(screen, other)

        self.velx -= force * math.sin(angle)
        self.vely += force * math.cos(angle)
        self.x += self.velx
        self.y -= self.vely