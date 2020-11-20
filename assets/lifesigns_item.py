#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This object is the superclass for other in-game objects."""

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

class LifesignsItem(object):
    """This object forms part of every in-game object."""

    def __init__(self, name="<unset>", description="<unset>"):
        self.__name = str(name)
        self.__description = str(description)


    # PROPERTY MODIFIERS > GETTERS


    def get_name(self):
        """Return private attribute '__name'."""
        return self.__name


    def get_description(self):
        """Return private attribute '__description'."""
        return self.__description


    # PROPERTY MODIFIERS > SETTERS


    def set_forename(self, name):
        """Mutate private attribute '__name'."""
        self.__name = name


    def set_description(self, description):
        """Mutate private attribute '__name'."""
        self.__description = description


# End of File.
