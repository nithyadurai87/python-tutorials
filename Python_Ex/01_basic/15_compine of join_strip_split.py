"""Combine of join,split,strip using one line for loop"""

v="      About  \n  IEE    \n jjd"
print v

#one line for loop
print " ".join(x.strip() for x in v.split("\n"))




