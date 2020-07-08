#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###########
# License #
###########

# Lifesigns Engine: A Python-based text adventure game engine.
# Copyright (C) 2020 William Willis Whinn

# This program is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If
# not, see <http://www.gnu.org/licenses/>.

##############
# Directives #
##############

# pylint: disable=too-many-arguments
# pylint: disable=too-few-public-methods

#####################
# Object Properties #
#####################

"""
- EMail
    - name (String)
        This is the name of the object.
    - description (String)
        This is a short description of the object.
    - sender (String)
        This should contain the name of the character who sent this message.
    - recipient (String)
        This value should hold the name of the person who received this object.
    - datestamp (String)
        This value should contain a nicely-formatted date for viewing only.
    - subject (String)
        This value should hold the subject line for the object.
    - contents (String)
        This should contain the main body text of the message itself.
"""

###########
# Objects #
###########

class EMail(object):
    """This object represents an E-Mail message."""
    name = ""
    description = ""
    sender = ""
    recipient = ""
    datestamp = ""
    subject = ""
    contents = ""

    def __init__(self, name, description, sender, recipient, datestamp,
                 subject, contents):
        self.name = name
        self.description = description
        self.sender = sender
        self.recipient = recipient
        self.datestamp = datestamp
        self.subject = subject
        self.contents = contents

    def read(self):
        """Display the contents of the E-Mail."""
        print("SUBJECT: {0}".format(self.subject))
        print("FROM: {0}".format(self.sender))
        print("TO: {0}".format(self.recipient))
        print("SENT: {0}\n".format(self.datestamp))
        print("MESSAGE BODY:\n{}".format(self.contents))

# End of File.
