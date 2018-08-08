#!/usr/bin/env python3

##########
# Notice #
##########

"""
Lifesigns Engine: A Python-based text adventure game engine.
Copyright (C) 2018 William Willis Whinn

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

##############
# Directives #
##############

# pylint: disable=unused-import

###########
# Imports #
###########

# Documents
from assets.email import EMail
from assets.journal import Journal
from assets.sticky_note import StickyNote

# Keys
from assets.metal_key import MetalKey
from assets.programmable_keycard import ProgrammableKeycard

# Weapons
from assets.firearm import Firearm

# Containers
from assets.inventory import Inventory

#############
# Variables #
#############

LIFESIGNS_METADATA_VERSION = '0.0.1'
LIFESIGNS_METADATA_URL = 'https://github.com/ultraviolet-1986/lifesigns-engine-python'

#############
# Functions #
#############

def display_prompt():
    """ Display the main Lifesigns Engine header """
    print("Lifesigns Engine v{} Copyright (C) 2018 William Whinn".
          format(LIFESIGNS_METADATA_VERSION))
    print(LIFESIGNS_METADATA_URL)

#############
# Kickstart #
#############

display_prompt()

# End of File.