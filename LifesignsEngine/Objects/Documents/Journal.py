#!/usr/bin/env python3


class Journal(object):
    name = ""
    description = ""
    contents = []

    def __init__(self, name, description, contents):
        self.name = name
        self.description = description
        self.contents = contents

    def read(self):
        print(self.name, "\n")
        for page in self.contents:
            print(page, "\n")

# End of File.
