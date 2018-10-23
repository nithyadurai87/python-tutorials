'''
matching alpha numeric charecters
^ defines the starting of the string
$ defines the ending of the string
+ defines one or more occurance
'''

import re

pattern = re.compile(r'^[A-Z0-9a-z]+$')

'''
Also the below pattern will do the same
pattern = re.compile(r'^\w+$')
\w -> matches alphanumeric
\W -> matches non alphanumeric
'''

string = input("Enter the string: ")

matches = pattern.search(string)

if matches:
    print("String matches")
else:
    print("Did not match")


