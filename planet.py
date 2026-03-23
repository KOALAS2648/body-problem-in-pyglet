import pyglet
from pyglet import shapes
if __name__ == "__main__":
    import types
class Planet(shapes.Circle):
    def __init__(self, x, y, radius, mass, segments = None, color = ..., blend_src = ..., blend_dest = ..., batch = None, group = None, program = None):
        super().__init__(x, y, radius, segments, color, blend_src, blend_dest, batch, group, program)
        self.x = x
        self.y = y
        self.mass = mass
