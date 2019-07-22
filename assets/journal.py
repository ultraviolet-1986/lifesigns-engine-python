#!/usr/bin/env python3

##########
# Notice #
##########

# Lifesigns Engine: A Python-based text adventure game engine.
# Copyright (C) 2019 William Willis Whinn

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#####################
# Object Properties #
#####################

"""
- Journal
    - name (String)
        This is the name of the object.
    - description (String)
        This is a short description of the object.
    - contents (Array, String)
        This should be a short paragraph per page.
    - legible (Boolean)
        - This determines whether or not the Journal can be read.
"""

###########
# Objects #
###########

class Journal(object):
    """ This object represents a multiple-paged paper Journal. """
    name = ""
    description = ""
    contents = []
    legible = False

    def __init__(self, name, description, contents, legible):
        self.name = name
        self.description = description
        self.contents = contents
        self.legible = legible

    def read(self):
        """ Display the contents of the Journal. """
        print("{0}\n".format(self.name))
        for page in self.contents:
            print("{0}\n".format(page))

    def damage(self):
        """ Damage the Journal. """
        if self.legible:
            self.legible = False

# End of File.
