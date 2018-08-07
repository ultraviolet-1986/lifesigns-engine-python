#!/usr/bin/env python3

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
    """ This object represents a small Metal Key used in traditional locks. """
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
        """ Repair the Metal Key if damaged, and allow use. """
        if not self.usable:
            self.usable = True
            print("Your {} has been repaired".format(self.name))
        else:
            print("Your {} does not need to be repaired".format(self.name))

    def damage(self):
        """ Damage the Metal Key and prevent use. """
        if self.usable:
            self.usable = False
            print("Your {} has been damaged".format(self.name))
        else:
            print("Your {} is already damaged".format(self.name))

# End of File.
