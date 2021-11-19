#!/usr/bin/env python3

print("hello, world!")
x = "x"
while x != "":
    x = input("Give me any string of text (empty string ends the program)\n> ")
    if x != "":
        print("You typed '" + x + "'")

print("Bye!")