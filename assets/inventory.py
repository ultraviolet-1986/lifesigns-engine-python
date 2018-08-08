#!/usr/bin/env python3

##########
# Notice #
##########

# Lifesigns Engine: A Python-based text adventure game engine.
# Copyright (C) 2018 William Willis Whinn

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
