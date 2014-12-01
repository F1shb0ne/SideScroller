import pyglet

from Game import *
from Graphics import *
from Keyboard import *

# Initialize window
window = pyglet.window.Window()

window.set_vsync(False)

# Graphics object, pass a reference to the Pyglet window object to it
gfx = Graphics(window)

# Keyboard object
kbd = Keyboard()

# The one and only game instance, pass it the graphics and keyboard object
game = Game(gfx, kbd)

@window.event
def on_draw():
    gfx.Update()

@window.event
def on_key_press(symbol, modifiers):
    kbd.SetKey(symbol)    

@window.event
def on_key_release(symbol, modifiers):
    kbd.ClearKey(symbol)    

# register game logic routine; 25 ticks per second
pyglet.clock.schedule_interval(game.Tick, 0.04)

pyglet.app.run()
