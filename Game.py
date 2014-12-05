from Player import *
from Graphics import *
from Map import *

class Game:
    # Initialize the game object
    def __init__(self, gfxObject, kbdObject):
        # Store the graphics and keyboard object
        self.gfx = gfxObject
        self.kbd = kbdObject

        # Init the map object
        self.m = Map()
        self.m.Load('forest1')

        # Init the player object
        self.p = Player(self.m.getStartX(), self.m.getStartY())
        # Tell the player about the game object
        self.p.SetGameObject(self)

        # Tell the Graphics object about the Game object
        self.gfx.SetGameObject(self)

        # Keep track of game ticks over time
        self.GameTick = 0

        self.isFalling = False
        self.PlayerFallAmount = 0
        self.PlayerFallDelay = 0
        self.PlayerFallPath = [1, 2, 4, 5, 7, 9, 10, 12, 14, 16, 19, 24]
        self.PlayerFallPathLength = 12
        self.PlayerFallPathIndex = 0

        self.isJumping = False
        self.wasJumping = False
        #self.PlayerJumpPath = [13, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
        self.PlayerJumpPath = [16, 14, 12, 10, 9, 7, 5, 4, 2, 1]
        self.JumpPathLength = 10
        self.PlayerJumpDelay = 0
        self.PlayerJumpPathIndex = 0
        self.NextJumpTick = 0
        self.jumpLatch = False


    def Tick(self, SomethingElse):

        px = self.p.GetPosX()
        py = self.p.GetPosY()


        self.GameTick += 1

        """ Jumping """
        # Reset jump latch
        if (self.kbd.A == False and self.jumpLatch == True):
            self.jumpLatch = False

        # Jump condition
        if (self.kbd.A == True and self.jumpLatch == False):
            if not self.isFalling:
                self.jumpLatch = True
                self.isJumping = True
                self.wasJumping = True
                self.NextJumpTick = self.GameTick + 1
                self.p.MoveVertical(self.PlayerJumpPath[self.PlayerJumpPathIndex])

        # Button released during mid-jump
        if (self.kbd.A == False and self.isJumping == True):
            self.isJumping = False
            self.PlayerJumpPathIndex = 0

        # Process height gained by player over time
        if (self.isJumping == True):
            self.PlayerJumpPathIndex += 1
            if self.PlayerJumpPathIndex > self.JumpPathLength-1:
                self.PlayerJumpPathIndex = 0
                self.isJumping = False
            else:
                self.p.MoveVertical(self.PlayerJumpPath[self.PlayerJumpPathIndex])


        """ Left & right movement """
        if (self.kbd.Left == True and self.kbd.Right == True) or (self.kbd.Left == False and self.kbd.Right == False):
            # This condition occurs if the player is holding left & right at the same time: freeze player
            self.p.SpriteID = 3
        else:
            if self.kbd.Left == True:
                # Check if something is in the way to the left
                if not (self.m.isSolid(px + 2, py + 1) or self.m.isSolid(px + 2, py + 63)):
                    self.p.MoveLeft()

            if self.kbd.Right == True:
                # Check if something is in the way to the right
                if not (self.m.isSolid(px + 30, py + 1) or self.m.isSolid(px + 30, py + 63)):
                    self.p.MoveRight()

        if not self.isJumping:
            self.PlayerFallTick()

    def PlayerFallTick(self):
        px = self.p.GetPosX()
        py = self.p.GetPosY()

        if self.m.isSolid(px + 3, py-1) or self.m.isSolid(px + 29, py-1):
            if self.isFalling == True:
                self.isFalling = False
                self.wasJumping = False
                self.PlayerFallAmount = 0
                self.PlayerFallPathIndex = 0
        else:
            self.isFalling = True

            self.PlayerFallPathIndex += 1
            if self.PlayerFallPathIndex >= self.PlayerFallPathLength:
                self.PlayerFallPathIndex = self.PlayerFallPathLength - 1

            self.PlayerFallAmount = self.PlayerFallPath[self.PlayerFallPathIndex]

            while self.m.isSolid(px + 3, py - self.PlayerFallAmount) or self.m.isSolid(px + 29, py - self.PlayerFallAmount):
                # Keep nudging the player up until flush with the floor surface
                self.PlayerFallAmount -= 1
            self.p.MoveVertical(-self.PlayerFallAmount)

