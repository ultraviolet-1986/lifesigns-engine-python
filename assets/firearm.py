#!/usr/bin/env python3

##############
# Directives #
##############

# pylint: disable=too-many-arguments

#####################
# Object Properties #
#####################

"""
- Firearm
    - name (String)
        This is the name of the object.
    - description (String)
        This is a short description of the object.
    - damage_inflicted (Integer)
        This value determines how powerful the weapon is.
    - capacity (Integer)
        This value holds the maximum bullet capacity of the object.
    - rounds_remaining (Integer)
        This value holds the number of bullets the object has remaining.
    - clips_remaining (Integer)
        This value shows how many clips the player has in their inventory.
    - usable (Boolean)
        This determines whether or not the weapon can be used or fired.
"""

###########
# Objects #
###########

class Firearm(object):
    """ This object represents a Firearm such as a Handgun or Rifle (etc.) """
    name = ""
    description = ""
    damage_inflicted = 0
    capacity = 0
    rounds_remaining = 0
    clips_remaining = 0
    usable = False

    def __init__(self, name, description, damage_inflicted, capacity,
                 rounds_remaining, clips_remaining, usable):
        self.name = name
        self.description = description
        self.damage_inflicted = damage_inflicted
        self.capacity = capacity
        self.rounds_remaining = rounds_remaining
        self.clips_remaining = clips_remaining
        self.usable = usable

    def add_clip(self):
        """ Add another clip to the Inventory. """
        self.clips_remaining += 1
        print("Your {} now has {} clip(s) remaining".format(
            self.name, self.clips_remaining))

    def fire_at(self, target):
        """ Fire the weapon and deal damage to the target. """
        if self.rounds_remaining > 0:
            self.rounds_remaining -= 1
            target.remaining_health -= self.damage_inflicted
        else:
            print("Your {} needs to be reloaded".format(self.name))

    def reload(self):
        """ Reload the weapon and remove a clip from the Inventory. """
        if self.clips_remaining > 0:
            self.clips_remaining -= 1
            self.rounds_remaining = self.capacity
            print("Your {} now has {} round(s) remaining".format(
                self.name, self.rounds_remaining))
            print("Your {} now has {} clips(s) remaining".format(
                self.name, self.clips_remaining))
        elif self.rounds_remaining > 0:
            print("Your {} still has {} round(s) loaded".format(
                self.name, self.rounds_remaining))
        else:
            print("You have no remaining ammunition")

# End of File.
