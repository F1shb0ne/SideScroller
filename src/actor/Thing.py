""" Things """

import src.actor.Actor

"""
    A Thing base class is any object that is neither the player or an NPC, but anything else.
    These can be a door, a chest or perhaps moving structures.
"""


class Thing(src.actor.Actor):
    def __init__(self, name, x, y):
        super(Thing, self).__init__(name, x, y)
