#!/usr/bin/env python3

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
    """ This object represents a small paper Sticky Note. """
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
        """ Display the contents of the Sticky Note. """
        if self.legible:
            print(self.contents)
        else:
            print("The note is illegible and cannot be read.")

    def damage(self):
        """ Damage the Sticky Note. """
        if self.legible:
            self.legible = False

# End of File.
