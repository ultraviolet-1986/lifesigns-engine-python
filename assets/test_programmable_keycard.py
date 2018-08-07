#!/usr/bin/env python3

""" This file is a unit test for 'programmable_keycard.py'. """

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
