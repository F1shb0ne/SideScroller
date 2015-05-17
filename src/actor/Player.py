""" Player """

import src.actor.Actor

"""
The Player class represents the player in the game.
"""


class Player(src.actor.Actor):
    def __init__(self, name, x, y):
        super(Player, self).__init__(name, x, y)
