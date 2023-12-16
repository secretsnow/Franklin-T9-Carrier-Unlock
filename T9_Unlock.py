#!/usr/bin/env python

from __future__ import print_function # enables the print function in Python 2
import hashlib # imports the hashlib module for computing hashes
import sys # imports the sys module for accessing standard input and output

print("Enter your IMEI: ", end="") # prints a prompt without a newline
IMEI = sys.stdin.readline().strip() # reads a line from standard input and removes the trailing newline
hash = hashlib.sha1(IMEI + "simlock").hexdigest()[:8] # computes SHA1 hash of the IMEI concatenated with "simlock" and takes the first 8 characters
print(hash, end="") # prints the hash without a newline
