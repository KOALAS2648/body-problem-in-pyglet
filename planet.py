import pyglet
from pyglet import shapes
from pyglet.gl import GL_SRC_ALPHA, GL_ONE
class Planet(shapes.Circle):
    def __init__(self, x, y, radius, mass, segments = None, color = (255,255,255), blend_src = GL_SRC_ALPHA, blend_dest = GL_ONE, batch = None, group = None, program = None):
        super().__init__(x, y, radius, segments, color, blend_src, blend_dest, batch, group, program)
        self.x = x
        self.y = y
        self.mass = mass
