import pyglet
from pyglet.window import key
from planet import *
from spaceship import *
from pyglet.graphics import Batch
class Window(pyglet.window.Window):
    def __init__(self, width, height, name):
        super().__init__(width, height, name, resizable=True)
        self.fps_display = pyglet.window.FPSDisplay(window=self)
        self.width = width
        self.height = height
        self.G =100
        self.batch = Batch()
        self.planet = Planet(self.width//2, self.height//2, 100, 100, color=(255, 76, 148), batch=self.batch)
        self.a1 = Spaceship(startx=200, starty=400, xvel=0, yvel=2, mass=1, radius=10, visible=True, color=(50, 225, 30), batch=self.batch)
        self.spaceships = [self.a1]
        self.startMousex = 0
        self.startMousey = 0
        self.deltax = 0
        self.deltay = 0
        self.clock = pyglet.clock.Clock()
    def on_draw(self):
        self.clock.tick()
        self.clear()
        self.fps_display.draw()
        self.planet.draw()
        self.batch.draw()
    def on_mouse_press(self, x, y, button, modifiers):
        self.startMousex = x
        self.startMousey = y
    def on_mouse_release(self, x, y, button, modifiers):
        self.deltax = self.startMousex - x
        self.deltay = y - self.startMousey
        self.add_obj(self.deltax, self.deltay)
    def add_obj(self, deltax, deltay):
        self.spaceships.append(Spaceship(self.startMousex, self.startMousey, deltax//3, deltay//3, 10, 10, visible=True, color=(255,45, 175), batch=self.batch))
    def update(self, dt):
        for ship in self.spaceships:
            ship.move(self, other=self.planet)

if __name__ == "__main__":
    screen = Window(800, 1000, "3 body program")
    screen.clock.schedule_interval(screen.update, 1/120.0)
    
    pyglet.app.run()