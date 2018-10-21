"""System argument -Program"""

#import System argument
import sys
print(sys.argv)

#From the  User
#User gives 4 or above 4 arguments
if(len(sys.argv)>=4):
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    c=int(sys.argv[3])

#User gives only 1 argument
elif(len(sys.argv)==1):
    a=input("Enter 1st Number: ")
    b=input("Enter 2nd Number: ")
    c=input("Enter 3rd Number: ")

#User gives 2 arguments
elif(len(sys.argv)==2):
    a=int(sys.argv[1])
    b=input("Enter 2nd Number: ")
    c=input("Enter 3rd Number: ")

#User gives 3 arguments
elif(len(sys.argv)==3):
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    c=input("Enter 3rd Number: ")


#Find the largest number
if(a>b and a>c):
    print("Largest Number is: %d" %a)
elif(b>c):
    print("Largest Number is: %d" %b)
else:
    print("Largest Number is: %d" %c)


