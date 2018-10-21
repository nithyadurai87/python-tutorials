
"""System argument -Program"""

import sys
print(sys.argv)

#Get three Numbers
a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])

#Find the largest number

if(a>b and a>c):
    print("Largest Number is: %d" %a)
elif(b>c):
    print("Largest Number is: %d" %b)
else:
    print("Largest Number is: %d" %c)
