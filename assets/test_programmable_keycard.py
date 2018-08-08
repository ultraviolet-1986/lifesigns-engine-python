#!/usr/bin/env python3

##########
# Notice #
##########

# Lifesigns Engine: A Python-based text adventure game engine.
# Copyright (C) 2018 William Willis Whinn

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

###########
# Imports #
###########

# System
import unittest

# Game Assets
from programmable_keycard import ProgrammableKeycard

###########
# Objects #
###########

TEST_KEY_CARD = ProgrammableKeycard(
    "Test Programmable Keycard Name",
    "Test Programmable Keycard Description",
    0,
    False
)

##############
# Unit Tests #
##############

class TestProgrammableKeycard(unittest.TestCase):
    """ Unit tests for the ProgrammableKeycard object. """

    def test_card_active(self):
        """ Test the activation of a Programmable Keycard. """
        TEST_KEY_CARD.activate()
        self.assertTrue(TEST_KEY_CARD.active)

    def test_card_inactive(self):
        """ Test the deactivation of a Programmable Keycard. """
        TEST_KEY_CARD.deactivate()
        self.assertFalse(TEST_KEY_CARD.active)

#############
# Kickstart #
#############

if __name__ == '__main__':
    unittest.main()

# End of File.
