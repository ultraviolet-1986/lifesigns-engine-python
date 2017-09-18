#!/usr/bin/env python3


class StickyNote(object):
    name = ""
    description = ""
    contents = ""

    def __init__(self, name, description, contents):
        self.name = name
        self.description = description
        self.contents = contents

    def read(self):
        print(self.contents)

# End of File.
