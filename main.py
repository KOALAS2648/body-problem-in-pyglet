import pyglet
from pyglet.window import key
from planet import *
from spaceship import *
from pyglet.graphics import Batch
class Window(pyglet.window.Window):
    def __init__(self, width, height, name):
        super().__init__(width, height, name, resizable=True)
        self.width = width
        self.height = height
        self.G =100
        self.batch = Batch()
        self.planet = Planet(self.width//2, self.height//2, 100, 100, color=(255, 76, 148), batch=self.batch)
        self.a1 = Spaceship(200, 400, 0, 2, 2, 10, color=(50, 225, 30), batch=self.batch)
        self.spaceships = [self.a1] 
    def on_draw(self):
        self.clear()
        self.batch.draw()
    def update(self, dt):
        self.a1.move(self, other=self.planet)
if __name__ == "__main__":
    screen = Window(800, 1000, "3 body program")
    pyglet.clock.schedule_interval(screen.update, 1/60.0)
    pyglet.app.run()