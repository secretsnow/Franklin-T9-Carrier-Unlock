#!/usr/bin/env python
# provide system functions
import sys
# provide hash algorithms 
import hashlib

 # display a prompt without a newline 
print("Enter your IMEI: ", end=""
# read a line from standard input and remove the trailing newline
IMEI = (
    sys.stdin.readline().strip()
)
# compute SHA1 hash of the input, then convert it to hexadecimal
hash = hashlib.sha1(
    (IMEI + "simlock").encode()
).hexdigest()
# print first 8 characters of the hash
print(hash[:8])
