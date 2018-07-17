#!/usr/bin/env python3


class Inventory(object):
    def __init__(self):
        self.inventory = []

    def list_items(self):
        if not self.inventory:
            print("Your inventory is empty")
        else:
            for item in self.inventory:
                if item == self.inventory[-1]:
                    print(item.name)
                    print(item.description)
                else:
                    print(item.name)
                    print(item.description)
                    print()

    def add_item(self, item):
        if item:
            self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

# End of File.
