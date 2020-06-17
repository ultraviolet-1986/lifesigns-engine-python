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

# Lifesigns Engine metadata and main header.

from .lifesigns_engine import display_prompt

# Colours and text formatting.

from .colours import BLUE
from .colours import CYAN
from .colours import GREEN
from .colours import MAGENTA
from .colours import RED
from .colours import YELLOW

from .colours import LIGHT_BLUE
from .colours import LIGHT_CYAN
from .colours import LIGHT_GREEN
from .colours import LIGHT_MAGENTA
from .colours import LIGHT_RED
from .colours import LIGHT_YELLOW

from .colours import BLACK
from .colours import GREY
from .colours import GRAY
from .colours import WHITE

from .colours import BOLD
from .colours import UNDERLINE

from .colours import COLOUR_RESET

# Lifesigns Engine assets.

from .assets import EMail
from .assets import Firearm
from .assets import Inventory
from .assets import Journal
from .assets import MetalKey
from .assets import ProgrammableKeycard
from .assets import StickyNote

#############
# Kickstart #
#############

display_prompt()

# End of File.
