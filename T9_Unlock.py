#!/usr/bin/env python

# provides system functions
import sys

# provides hash algorithms 
import hashlib

 # display prompt w/o a newline 
print("Enter your IMEI: ", end="")

# read line from standard input & remove the trailing newline
IMEI = (
    sys.stdin.readline().strip()
)

# compute SHA1 hash of input, then convert it to hexadecimal
hash = hashlib.sha1(
    (IMEI + "simlock").encode()
).hexdigest()

# print first 8 chars of hash
print(hash[:8])

