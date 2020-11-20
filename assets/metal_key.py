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

#####################
# Object Properties #
#####################

"""
- MetalKey
    - name (String)
        This is the name of the object.
    - description (String)
        This is a short description of the object.
    - unlock_target (String)
        This determines which door the key can unlock.
    - usable (Boolean)
        This determines whether or not the key has succumbed to damage.
"""

###########
# Objects #
###########

class MetalKey(object):
    """This object represents a small Metal Key used in traditional locks."""
    name = ""
    description = ""
    unlock_target = ""
    usable = False

    def __init__(self, name, description, unlock_target, usable):
        self.name = name
        self.description = description
        self.unlock_target = unlock_target
        self.usable = usable

    def repair(self):
        """Repair the Metal Key if damaged, and allow use."""
        if not self.usable:
            self.usable = True
            print("Your {0} has been repaired".format(self.name))
        else:
            print("Your {0} does not need to be repaired".format(self.name))

    def damage(self):
        """Damage the Metal Key and prevent use."""
        if self.usable:
            self.usable = False
            print("Your {0} has been damaged".format(self.name))
        else:
            print("Your {0} is already damaged".format(self.name))

# End of File.
