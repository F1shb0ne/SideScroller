import pyglet
from Player import *
from Game import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Graphics:
    def __init__(self, PygletObject):
        # This holds the Pyglet window object
        self.PyWin = PygletObject

        self.GameObject = None

        # These are points to be drawn at the end of each frame for debugging
        self.PointList = []

        self.OffsetX = 0
        self.fOffsetY = 0

        """ Load external game resources """

        # Right-facing sprite data for player
        self.s_link_stand_r = pyglet.resource.image('gfx/player/link-stand-r.png')
        self.s_link_walk1_r = pyglet.resource.image('gfx/player/link-walk1-r.png')
        self.s_link_walk2_r = pyglet.resource.image('gfx/player/link-walk2-r.png')
        self.s_link_walk3_r = pyglet.resource.image('gfx/player/link-walk3-r.png')

        # Left-facing sprite data for player
        self.s_link_stand_l = pyglet.resource.image('gfx/player/link-stand-l.png')
        self.s_link_walk1_l = pyglet.resource.image('gfx/player/link-walk1-l.png')
        self.s_link_walk2_l = pyglet.resource.image('gfx/player/link-walk2-l.png')
        self.s_link_walk3_l = pyglet.resource.image('gfx/player/link-walk3-l.png')

        # Map background tiles
        self.bg_bushes = pyglet.resource.image('gfx/forest/bushes.png')
        self.bg_forest_floor = pyglet.resource.image('gfx/forest/forest-floor.png')
        self.bg_leaves = pyglet.resource.image('gfx/forest/leaves.png')
        self.bg_leaves_bottom = pyglet.resource.image('gfx/forest/leaves-bottom.png')
        self.bg_tree_trunk = pyglet.resource.image('gfx/forest/tree-trunk.png')
        #self.bg_test = pyglet.resource.image('gfx/forest/test.png')

    def SetGameObject(self, GameInstance):
        self.GameObject = GameInstance

    def Update(self):
        self.PyWin.clear()
        self.DrawBackground()
        self.DrawPlayer()
        #self.DrawPoints()

    def QueuePoint(self, x, y):
        self.PointList.append(Point(x, y))

    def DrawPoints(self):
        for i in range(0, len(self.PointList)):
            pyglet.graphics.draw(1, pyglet.gl.GL_POINTS,
                ('v2i', (self.PointList[i].x, self.PointList[i].y)),
                ('c3B', (255, 255, 255))
            )
        self.PointList = []

    def DrawBackground(self):
        for x in range(0, 20):
            for y in range(0, 15):
                tile = self.GameObject.m.getTileID(x, y)
                if tile == 1:
                    self.bg_forest_floor.blit(x*32, y*32)
                if tile == 2:
                    self.bg_leaves.blit(x*32, y*32)
                if tile == 3:
                    self.bg_leaves_bottom.blit(x*32, y*32)
                if tile == 4:
                    self.bg_tree_trunk.blit(x*32, y*32)
                if tile == 5:
                    self.bg_bushes.blit(x*32, y*32)

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
