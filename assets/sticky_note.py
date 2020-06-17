#!/usr/bin/env python3

##########
# Notice #
##########

# Lifesigns Engine: A Python-based text adventure game engine.
# Copyright (C) 2020 William Willis Whinn

# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.

# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

###########
# Imports #
###########

from ..colours import BOLD
from ..colours import GREEN
from ..colours import RED
from ..colours import YELLOW
from ..colours import COLOUR_RESET

#####################
# Object Properties #
#####################

"""
- StickyNote
    - name (String)
        This is the name of the object.
    - description (String)
        This is a short description of the object.
    - contents (String)
        This should be a short message or passphrase.
    - legible (Boolean)
        - This determines whether or not the Sticky Note can be read.
"""

###########
# Objects #
###########

class StickyNote(object):
    """This object represents a small paper Sticky Note."""
    name = ""
    description = ""
    contents = ""
    legible = False

    def __init__(self, name, description, contents, legible):
        self.name = name
        self.description = description
        self.contents = contents
        self.legible = legible

    def read(self):
        """Display the contents of the Sticky Note."""
        if self.legible:
            print("> Item \"{0}\" reads:".format(self.name))
            print("  {0}\"{1}\"{2}\n".format(YELLOW,
                                           self.contents,
                                           COLOUR_RESET))
        else:
            print("> {0}Item \"{1}\" is illegible and cannot be read.{2}\n"
                  .format(RED, self.name, COLOUR_RESET))

    def damage(self):
        """Damage the Sticky Note."""
        if self.legible:
            self.legible = False

# End of File.
