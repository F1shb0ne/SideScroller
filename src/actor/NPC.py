""" NPC """

"""
The NPC base class inherits from Actor.
These can represent villagers, animals, monsters etc
"""

import src.actor.Actor


class NPC(src.actor.Actor):
    def __init__(self, name, x, y):
        super(NPC, self).__init__(name, x, y)


class Ally(NPC):
    def __init__(self, name, x, y):
        super(Ally, self).__init__(name, x, y)
        current_sprite = None
        anim_step = 1

    def animate(self):
        pass
