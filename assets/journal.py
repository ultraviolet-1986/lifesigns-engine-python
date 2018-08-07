#!/usr/bin/env python3

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
        print(self.name, "\n")
        for page in self.contents:
            print(page, "\n")

    def damage(self):
        """ Damage the Journal. """
        if self.legible:
            self.legible = False

# End of File.
