#!/usr/bin/env python3


class EMail(object):
    name = ""
    description = ""
    sender = ""
    recipient = ""
    datestamp = ""
    subject = ""
    contents = ""

    def __init__(self, name, description, sender, recipient, datestamp, subject, contents):
        self.name = name
        self.description = description
        self.sender = sender
        self.recipient = recipient
        self.datestamp = datestamp
        self.subject = subject
        self.contents = contents

    def read(self):
        print("SUBJECT:", self.subject)
        print("FROM:", self.sender)
        print("TO:", self.recipient)
        print("SENT:", self.datestamp, "\n")
        print("MESSAGE BODY:")
        print(self.contents)

# End of File.
