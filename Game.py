from Player import *
from Graphics import *

class Game:

    # Initialize the game object
    def __init__(self, gfxObject, kbdObject):
        # Store the graphics and keyboard object
        self.gfx = gfxObject
        self.kbd = kbdObject
        
        # Init the player object
        self.p = Player(0, 0)

        # Tell the Graphics object about the Game object
        self.gfx.SetGameObject(self)
        
        # Keep track of game ticks over time
        self.GameTick = 0
        
        

        # temporary limit for debugging
        self.GameTickLimit = 100

    def Tick(self, SomethingElse):

        self.GameTick += 1

        if ((self.kbd.Left == True) and (self.kbd.Right == True)) or ((self.kbd.Left == False and self.kbd.Right == False)):
            self.p.SpriteID = 3 # halt
        else:
            if self.kbd.Left == True:
                self.p.MoveLeft()
                
            if self.kbd.Right == True:
                self.p.MoveRight()
        

