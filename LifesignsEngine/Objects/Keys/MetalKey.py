#!/usr/bin/env python3


class MetalKey(object):
    name = ""
    description = ""
    unlock_target = ""
    is_rusted = False

    def __init__(self, name, description, unlock_target, is_rusted):
        self.name = name
        self.description = description
        self.unlock_target = unlock_target
        self.is_rusted = is_rusted

    def repair(self):
        if self.is_rusted == True:
            self.is_rusted = False
            print("Your", self.name, "has been repaired")
        else:
            print("Your", self.name, "does not need to be repaired")

    def rust(self):
        if self.is_rusted == False:
            self.is_rusted = True
            print("Your", self.name, "has become rusty")
        else:
            print("Your", self.name, "is already rusty")

# End of File.
