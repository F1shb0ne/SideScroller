""" Actors """

"""
Base class for any entity in the game
"""


class Actor(object):
    def __init__(self, name, pos_x, pos_y):
        # Starting position
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        print "An actor named " + self.name + " has been declared!"
