'''
matching at the starting of the string
^ denotes the starting of the string in regex
'''

import re

pattern = re.compile(r'^hello')

string = input("Enter the string: ")

matches = pattern.search(string)

if matches:
    print("String matches")
else:
    print("Did not match")



