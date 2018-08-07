#!/usr/bin/env python3

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
    """ This object represents an E-Mail message. """
    name = ""
    description = ""
    sender = ""
    recipient = ""
    datestamp = ""
    subject = ""
    contents = ""

    def __init__(self, name, description, sender, recipient, datestamp, subject,
                 contents):
        self.name = name
        self.description = description
        self.sender = sender
        self.recipient = recipient
        self.datestamp = datestamp
        self.subject = subject
        self.contents = contents

    def read(self):
        """ Display the contents of the E-Mail. """
        print("SUBJECT:", self.subject)
        print("FROM:", self.sender)
        print("TO:", self.recipient)
        print("SENT:", self.datestamp, "\n")
        print("MESSAGE BODY:")
        print(self.contents)

# End of File.
