#!/usr/bin/env python3


class ProgrammableKeycard(object):
    name = ""
    description = ""
    clearance_level = 0
    is_active = False

    def __init__(self, name, description, clearance_level, is_active):
        self.name = name
        self.description = description
        self.clearance_level = clearance_level
        self.is_active = is_active

    def activate(self):
        if not self.is_active:
            self.is_active = True
            print("Your", self.name, "has now been activated")
        else:
            print("Your", self.name, "does not need to be activated")

    def deactivate(self):
        if self.is_active:
            self.is_active = False
            print("Your", self.name, "has been deactivated")
        else:
            print("Your", self.name, "is already deactivated")

# End of File.
