"""Get the input for python-Program"""


#Normal input
print("Here String inputs are closed with double quotes")
Name = input("Enter your Name: ")
Clg = input("Enter College Name: ")
Num = input("Enter Your Roll.NO: ")

#print the details
print("\n\nMy Name: %s\t College: %s\t Num: %d" %(Name,Clg,Num))

#Raw input
print("Here all inputs are Strings")
Name = raw_input("Enter your Name: ")
Clg = raw_input("Enter College Name: ")
Num = raw_input("Enter Your Roll.NO: ")


#print the details in  raw_input
#this line Num in %s using
print("\nthis line Num in %s using")
print("\n\nMy Name: %s\t College: %s\t Num: %s" %(Name,Clg,Num))


#this line change the type string to integer
Num=int(Num)


#this line Num in %d using
print("\nthis line Num in %d using")
print("\n\nMy Name: %s\t College: %s\t Num: %d" %(Name,Clg,Num))
