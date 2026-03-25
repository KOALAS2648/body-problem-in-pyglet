import pyglet
from pyglet import shapes
from pyglet.gl import GL_SRC_ALPHA, GL_ONE
import math
class Spaceship(shapes.Circle):
    def __init__(self, startx:int, starty:int, xvel:int, yvel:int, mass:int, radius:int, visible:bool=False, segments = None, color:tuple =(255,255,255),blend_src = GL_SRC_ALPHA, blend_dest = GL_ONE, batch = None, group = None, program = None):
        super().__init__(startx, starty, radius, segments, color, blend_src, blend_dest, batch, group, program)
        self.x = startx
        self.y = starty
        self.velx = xvel
        self.vely = yvel
        self.mass = mass
        self.visible = True
    def distance(self, other: object):
        return (other.x-self.x)**2 + (self.y-other.y)**2
    def get_force(self,screen,  other: object):
        force = other.gravity*(self.mass*other.mass / self.distance(other))
        return force
    def move(self, screen, other):
        self.wrap(screen=screen)
        otherx, othery = other.x, other.y
        deltax =other.x - self.x
        deltay = self.y - othery
        angle = math.atan2(deltay, deltax)
        force = self.get_force(screen, other)

        self.velx -= force * math.cos(angle)
        self.vely += force * math.sin(angle)
        self.x -= self.velx
        self.y -= self.vely
    def wrap(self, screen):
        if self.x+self.radius > screen.width:
            self.x = self.radius
        if self.x-self.radius < 0:
            self.x = screen.width-self.radius
        if self.y+self.radius > screen.height:
            self.y = self.radius
        if self.y-self.radius < 0:
            self.y = screen.height-self.radius
    def draw(self):
        if self.visible:
            return super().draw()