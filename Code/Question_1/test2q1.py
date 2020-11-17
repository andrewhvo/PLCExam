import os
import sys
import re
# Parses text file into an empty list r
f = open("question1.txt", "r")
r = f.read()
# converts the list of lists into a lists of strings as list_String
list_String = []
list_String = r.split( )

# iterates through the list of strings and assigns a token to every valid string
for i in list_String:
    # Uses regex to find any string that starts with @, $, or % 
    if(re.fullmatch("^(@|\$|%)[a-zA-Z0-9]+_?[a-zA-Z0-9]+", i)):
        print(i + ": " + "Pearl")
    # Uses regex to find any string that is within quotations 
    elif(re.fullmatch("^(\").*(\"$)", i)):
       print(i + ": " + "String")
    # Uses regex to find just numbers with a minimum of 1 digit char
    elif(re.fullmatch("[1-9][0-9]*", i)):
        print(i + ": " + "Decimal")
    # Uses regex to find numbers starting with 0 and digit chars consisting of 1-7
    elif(re.fullmatch("0[0-7]*", i)):
        print(i + ": " + "Octal")
    # Uses regex to find a number starting with 0x and ending with an optional suffix
    elif(re.fullmatch("0[xX][0-9a-fA-F]*", i)):
        print(i + ": " + "C-Style integer literal hex")
    # Finds any floating point with optional prefix, minimum of 1 digit and followed by a exponent
    elif(re.fullmatch("[-+]?([0-9]*[.])?[0-9]+([eE][-+]?\d+)?", i)):
        print(i + ": " + "C-Style float literal") 
    # Finds any string starting with a alpha, followed by optional underscore.
    elif(re.fullmatch("[a-zA-Z_][a-zA-Z_0-9]*", i)):
        print(i + ": " + "C-Style character literal")
    # Finds any non-alphanumberic char that was listed in the question
    elif(re.fullmatch("([+]|[=]|[\==]|[-]|[\]|[\\]|[\/]|[*]|[++]|[--]|[%]|[&&]|[||]|[!=]|[(]|[)]|[{]|[}])*", i)):
        print(i + ": " + "Non-Alphanumeric")
    else:
        print(i + ": " + "Invalid")
