import pyglet
from pyglet.window import key

class Keyboard:
    
    Up = False
    Down = False
    Left = False
    Right = False
    
    B = False
    A = False
    
    Select = False
    Start = False    
    
    def __init__(self):
        pass
    
    def SetKey(self, Key):
        if Key == key.W:
            self.Up = True
        if Key == key.A:
            self.Left = True
        if Key == key.S:
            self.Down = True
        if Key == key.D:
            self.Right = True
        
        if Key == key.TAB:
            self.Select = True
        if Key == key.ENTER:
            self.Start = True
    
        if Key == key.NUM_1:
            self.B = True
        if Key == key.NUM_2:
            self.A = True

    def ClearKey(self, Key):
        if Key == key.W:
            self.Up = False
        if Key == key.A:
            self.Left = False
        if Key == key.S:
            self.Down = False
        if Key == key.D:
            self.Right = False
        
        if Key == key.TAB:
            self.Select = False
        if Key == key.ENTER:
            self.Start = False
    
        if Key == key.NUM_1:
            self.B = False
        if Key == key.NUM_2:
            self.A = False
