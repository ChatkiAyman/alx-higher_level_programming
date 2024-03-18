#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if (ord(char) >= 97 and ord(char) <= 122):
            character = ord(char) - 32
            upperCase = chr(character)
            print("{:s}".format(upperCase), end="")
        else:
            print("{:s}".format(char), end="")
