#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###########
# License #
###########

# Lifesigns Engine: A Python-based text adventure game engine.
# Copyright (C) 2020 William Willis Whinn

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

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
    - damage_potential (Integer)
        This value determines how powerful the weapon is.
    - capacity (Integer)
        This value holds the maximum bullet capacity of the object.
    - rounds_remaining (Integer)
        This value holds the number of bullets the object has remaining.
    - magazines_remaining (Integer)
        This value shows how many magazines the player has in their inventory.
    - usable (Boolean)
        This determines whether or not the weapon can be used or fired.
"""

from lifesigns_item import LifesignsItem

###########
# Objects #
###########

class Firearm(LifesignsItem):
    """This object represents a Firearm such as a Handgun or Rifle (etc)."""


    def __init__(self, name, description, damage_potential=0, capacity=0,
                 rounds_remaining=0, magazines_remaining=0, usable=True):

        """Initialise the superclass and define the Firearm object."""

        # INITIALISE SUPERCLASS
        super().__init__()

        # OBJECT PROPERTIES
        self.name = name
        self.description = description
        self.damage_potential = damage_potential
        self.capacity = capacity
        self.rounds_remaining = rounds_remaining
        self.magazines_remaining = magazines_remaining
        self.usable = usable


    # STRING INTERPRETATION OF THE FIREARM OBJECT
    def __str__(self):
        """Display the object's status."""
        super(Firearm).__str__()

        return ("Your {0} has {1} round(s) and {2} magazine(s) remaining.\n"
                .format(self.name, self.rounds_remaining,
                        self.magazines_remaining))


    # OBJECT METHODS
    def add_magazine(self):
        """Add another magazine to the Inventory."""
        self.magazines_remaining += 1
        print("Your {0} now has {1} magazine(s) remaining.\n"
              .format(super().get_name(), self.magazines_remaining))


    def fire_at(self, target):
        """Fire the weapon and deal damage to the target."""
        if self.rounds_remaining > 0:
            self.rounds_remaining -= 1
            target.remaining_health -= self.damage_potential
        else:
            print("Your {0} must be reloaded.\n".format(self.name))


    def reload(self):
        """Reload the weapon and remove a magazine from the Inventory."""
        if self.magazines_remaining > 0:
            self.magazines_remaining -= 1
            self.rounds_remaining = self.capacity
            print(self)
        elif self.rounds_remaining > 0:
            print(self)
        else:
            print("You have no remaining ammunition.\n")


# End of File.
