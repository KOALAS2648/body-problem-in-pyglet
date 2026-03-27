import pyglet
from pyglet.window import key
from planet import *
from spaceship import *
from pyglet.graphics import Batch
from random import randint
class Window(pyglet.window.Window):
    def __init__(self, width, height, name):
        super().__init__(height, width, name, resizable=True)
        self.fps_display = pyglet.window.FPSDisplay(window=self)
        self.width = width
        self.height = height
        self.G =100
        self.batch = Batch()
        self.planet = Planet(self.width//2, self.height//2, 100, 100, color=(255, 76, 148, 255), batch=self.batch)
        self.a1 = Spaceship(startx=200, starty=400, xvel=0, yvel=2, mass=1, radius=10, visible=True, color=(50, 225, 30, 255), batch=self.batch)
        self.mouse_pressed = False
        self.spaceships = [self.a1, ]
        self.tempList = [Spaceship(startx=randint(0,self.width), starty=randint(0, self.height), xvel=randint(-10, 10), yvel=randint(-10, 10), mass=1, radius=10, visible=False, color=(50, 225, 30, 255), batch=self.batch) for _ in range(0, 10)]
        self.startMousex = 0
        self.startMousey = 0
        self.deltax = 0
        self.deltay = 0
        self.clock = pyglet.clock.Clock()
        self.drawLine = shapes.Line(self.startMousex, self.startMousey, 0, 0, 5, (255,67,92), batch=self.batch)
        self.set_caption = "testing"
        
    def on_draw(self):
        self.clock.tick()
        self.clear()
        self.fps_display.draw()
        self.planet.draw()
        
        self.batch.draw()
        if self.mouse_pressed:
            self.drawLine.draw()
        
    def on_mouse_press(self, x, y, button, modifiers):
        self.startMousex = x
        self.startMousey = y
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.mouse_pressed = True
        self.drawLine = shapes.Line(self.startMousex, self.startMousey, x, y, 5, (255,67,92))
    def on_mouse_release(self, x, y, button, modifiers):
        self.deltax = x - self.startMousex
        self.deltay = y - self.startMousey

        self.mouse_pressed = False
        self.add_obj(self.deltax, self.deltay)
    def add_obj(self, deltax, deltay):
        self.spaceships.append(Spaceship(self.startMousex, self.startMousey, deltax//10, deltay//10, 10, 10, visible=True, color=(255,45, 175, 255), batch=self.batch))

    def update(self, dt):
        
        [ship.move(self, other=self.planet) for ship in self.spaceships]
        [ship.move(self, other=self.planet) for ship in self.tempList]

if __name__ == "__main__":
    screen = Window(900, 1000, "3 body program")
    screen.clock.schedule_interval(screen.update, 1/120.0)
    
    pyglet.app.run()