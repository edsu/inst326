import os
import re
import codecs


class Email():

    def __init__(self, path):
        self.path = path
        fh = codecs.open(path, 'r', 'ISO-8859-1')
        self.text = fh.read()

    def get_from(self):
        match = re.search('From: (.+)', self.text)
        if match:
            return match.group(1)
        else:
            return None

    def get_to(self):
        match = re.search('To: (.+)', self.text)
        if match:
            emails = match.group(1).strip()
            return emails.split(',')
        else:
            return None

def get_emails():
    for dirpath, dirnames, filenames in os.walk('enron-sample'):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            email = Email(path)
            print('to', email.get_to())
            print('from', email.get_from())
