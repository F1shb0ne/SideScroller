import pyglet
from Player import *
from Game import *

class Graphics:
    def __init__(self, PygletObject):
        # This holds the Pyglet window object
        self.PyWin = PygletObject
        
        self.GameObject = None
        
        # Load external game resources
        self.s_link_stand_r = pyglet.resource.image('gfx/player/link-stand-r.png')
        self.s_link_walk1_r = pyglet.resource.image('gfx/player/link-walk1-r.png')
        self.s_link_walk2_r = pyglet.resource.image('gfx/player/link-walk2-r.png')
        self.s_link_walk3_r = pyglet.resource.image('gfx/player/link-walk3-r.png')

        self.s_link_stand_l = pyglet.resource.image('gfx/player/link-stand-l.png')
        self.s_link_walk1_l = pyglet.resource.image('gfx/player/link-walk1-l.png')
        self.s_link_walk2_l = pyglet.resource.image('gfx/player/link-walk2-l.png')
        self.s_link_walk3_l = pyglet.resource.image('gfx/player/link-walk3-l.png')

    def SetGameObject(self, GameInstance):
        self.GameObject = GameInstance
    
    def Update(self):
        self.PyWin.clear()        
        self.DrawPlayer()
    
    def DrawPlayer(self):

        self.PlayerSpriteID = self.GameObject.p.GetSpriteID()
        self.PosX = self.GameObject.p.GetPosX()
        self.PosY = self.GameObject.p.GetPosY()

        # blit sprite to screen according to which animation frame is being used
        if self.PlayerSpriteID == 0:
            if self.GameObject.p.FacingRight == True:            
                self.s_link_walk1_r.blit(self.PosX, self.PosY)
            else:
                self.s_link_walk1_l.blit(self.PosX, self.PosY)
                
        if self.PlayerSpriteID == 1:
            if self.GameObject.p.FacingRight == True:            
                self.s_link_walk2_r.blit(self.PosX, self.PosY)
            else:
                self.s_link_walk2_l.blit(self.PosX, self.PosY)

        if self.PlayerSpriteID == 2:
            if self.GameObject.p.FacingRight == True:            
                self.s_link_walk3_r.blit(self.PosX, self.PosY)
            else:
                self.s_link_walk3_l.blit(self.PosX, self.PosY)

        
        if self.PlayerSpriteID == 3:
            if self.GameObject.p.FacingRight == True:
                self.s_link_stand_r.blit(self.PosX, self.PosY)
            else:
                self.s_link_stand_l.blit(self.PosX, self.PosY)
