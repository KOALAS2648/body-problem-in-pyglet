import pyglet
from pyglet.window import key

class Window(pyglet.window.Window):
    def __init__(self, width, height, name):
        super().__init__(width, height, name, resizable=True)
        self.width = width
        self.height = height
        self.G =10
    def on_draw(self):
        pass
    def update(self, dt):
        pass
if __name__ == "__main__":
    screen = Window(400, 400, "3 body program")
    pyglet.clock.schedule_interval(screen.update, 1/60.0)
    pyglet.app.run()