#!/usr/bin/env python3


class Firearm(object):
    name = ""
    description = ""
    damage_inflicted = 0
    capacity = 0
    rounds_remaining = 0
    clips_remaining = 0
    is_usable = False

    def __init__(self, name, description, damage_inflicted, capacity, rounds_remaining, clips_remaining, is_usable):
        self.name = name
        self.description = description
        self.damage_inflicted = damage_inflicted
        self.capacity = capacity
        self.rounds_remaining = rounds_remaining
        self.clips_remaining = clips_remaining
        self.is_usable = is_usable

    def add_clip(self):
        self.clips_remaining += 1
        print("Your", self.name, "now has", self.clips_remaining, "clip(s) remaining")

    def fire_at(self, target):
        if self.rounds_remaining > 0:
            self.rounds_remaining -= 1
            target.remaining_health -= self.damage_inflicted
        else:
            print("Your", self.name, "needs to be reloaded")

    def reload(self):
        if self.clips_remaining > 0:
            self.clips_remaining -= 1
            self.rounds_remaining = self.capacity
            print("Your", self.name, "now has", self.rounds_remaining, "round(s) remaining")
            print("Your", self.name, "now has", self.clips_remaining, "clips(s) remaining")
        elif self.rounds_remaining > 0:
            print("Your", self.name, "still has", self.rounds_remaining, "round(s) loaded")
        else:
            print("You have no remaining ammunition")

# End of File.
