#!/usr/bin/env python
# This is the shebang line that tells the operating system which interpreter to use
from __future__ import print_function # This enables the print function in Python 2
import hashlib # This imports the hashlib module for computing hashes
import sys # This imports the sys module for accessing standard input and output

# Your code goes here
print("Enter your IMEI: ", end="") # This prints a prompt without a newline
IMEI = sys.stdin.readline().strip() # This reads a line from standard input and removes the trailing newline
hash = hashlib.sha1(IMEI + "simlock").hexdigest()[:8] # This computes the SHA1 hash of the IMEI concatenated with "simlock" and takes the first 8 characters
print(hash, end="") # This prints the hash without a newline
