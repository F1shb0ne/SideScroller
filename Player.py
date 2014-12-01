class Player:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.FacingRight = True
        self.SpriteID = 0     
        self.WalkAnimationStep = 0
        self.WalkAnimationFrame = 0   
        
    def MoveRight(self):
        self.FacingRight = True
        self.MoveRelative(3, 0)
    def MoveLeft(self):
        self.FacingRight = False
        self.MoveRelative(-3, 0)
    
    def MoveRelative(self, x, y):
        self.pos_x += x
        self.pos_y += y
        self.WalkAnimationStep += 1
        if self.WalkAnimationStep > 3:
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
    