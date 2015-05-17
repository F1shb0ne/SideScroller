# Main script for testing (dont count on it working)

import src.res.Sprite
import src.ResourceMgr

import sys
import pygame
import pygame.locals
from time import *

import src.actor.NPC

# Instantiate the only and only Game Resource object
GRes = src.ResourceMgr.GameResources()

pygame.init()
pygame.display.set_caption("Side-Scroller Demo")
screen = pygame.display.set_mode((512, 512))

terra = src.actor.NPC.Ally("terra", 50, 50)

while True:

    screen.fill((255, 255, 255))

    # screen.blit(GRes.frame["terra:walk_right:1"], (0 + x, 100))

    sleep(.03125)  # 32 fps

    # x += 1

    # pygame.display.flip()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

    """
    while pygame.event.wait().type != pygame.locals.QUIT:
        pass

    """
