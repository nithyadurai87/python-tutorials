"""If condition -Program"""

#Get three Numbers
a=input("Enter 1st Number: ")
b=input("Enter 2nd Number: ")
c=input("Enter 3rd Number: ")

#Find the largest number

if(a>b and a>c):
    print("Largest Number is: %d" %a)
elif(b>c):
    print("Largest Number is: %d" %b)
else:
    print("Largest Number is: %d" %c)
