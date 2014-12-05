
from Game import *

class Player:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.FacingRight = True
        self.SpriteID = 0
        self.WalkAnimationStep = 0
        self.WalkAnimationFrame = 0

        self.GameObject = None

    def SetGameObject(self, g):
        self.GameObject = g

    def MoveRight(self):
        if self.GameObject.isFalling and not self.GameObject.wasJumping:
            MoveSpeed = 2
        else:
            MoveSpeed = 5
        self.FacingRight = True
        self.MoveRelative(MoveSpeed, 0)
    def MoveLeft(self):
        if self.GameObject.isFalling and not self.GameObject.wasJumping:
            MoveSpeed = 2
        else:
            MoveSpeed = 5
        self.FacingRight = False
        self.MoveRelative(-MoveSpeed, 0)

    def MoveVertical(self, y):
        self.pos_y += y

    def MoveRelative(self, x, y):
        self.pos_x += x
        self.pos_y += y

        if not self.GameObject.isFalling:
            self.WalkAnimationStep += 1
            if self.WalkAnimationStep > 1:
                self.WalkAnimationStep = 0
                self.WalkAnimationFrame += 1
                if self.WalkAnimationFrame > 2:
                    self.WalkAnimationFrame = 0
                self.SpriteID = self.WalkAnimationFrame

    def Halt(self):
        self.SpriteID = 3

    def GetSpriteID(self):
        return self.SpriteID

    def GetPosX(self):
        return self.pos_x

    def GetPosY(self):
        return self.pos_y

    def tellPosition(self):
        print('Player is located at (' + str(self.pos_x) + ', ' + str(self.pos_y) + ')')
