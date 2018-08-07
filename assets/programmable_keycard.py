#!/usr/bin/env python3

#####################
# Object Properties #
#####################

"""
- ProgrammableKeycard
    - name (String)
        This is the name of the object.
    - description (String)
        This is a short description of the object.
    - clearance_level (Integer)
        This determines what level of door the keycard can unlock.
    - active (Boolean)
        This determines whether or not the card has been activated for use.
"""

###########
# Objects #
###########

class ProgrammableKeycard(object):
    """ This object represents a Programmable Keycard. """
    name = ""
    description = ""
    clearance_level = 0
    active = False

    def __init__(self, name, description, clearance_level, active):
        self.name = name
        self.description = description
        self.clearance_level = clearance_level
        self.active = active

    def activate(self):
        """ Activate the Programmable Keycard for use on compatible locks. """
        if not self.active:
            self.active = True
            print("Your", self.name, "has now been activated.")
        else:
            print("Your", self.name, "does not need to be activated.")

    def deactivate(self):
        """ Deactivate the Programmable Keycard and prevent use. """
        if self.active:
            self.active = False
            print("Your", self.name, "has been deactivated.")
        else:
            print("Your", self.name, "is already deactivated.")

# End of File.
