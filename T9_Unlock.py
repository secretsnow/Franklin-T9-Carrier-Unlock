#!/usr/bin/env python
import sys # provides access to system functions
import hashlib # provides hash algorithms
print("Enter your IMEI: ", end="") #  displays a prompt without a newline
IMEI = sys.stdin.readline().strip() # reads a line from standard input and removes the trailing newline
hash = hashlib.sha1((IMEI + "simlock").encode()).hexdigest() # computes SHA1 hash of input, then converts it to hexadecimal
print(hash[:8]) # prints first 8 chara of the hash
