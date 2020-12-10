'''
matching the string 
'''
import re

pattern = re.compile(r'hello')

string = input("Enter the string: ")

matches = pattern.search(string)

if matches:
    print("string matches")

else:
    print("Did not match")
