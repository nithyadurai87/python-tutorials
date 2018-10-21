"""List operation"""

#initial list
a=[9,7,8,2,77,34]

#print the list

print ("\nList is: ");
print (a);

    
#Index value of given input
print("\n\n****Find Index Value****")
print("\nIndex value of no 2 is:")
print a.index(2)

print("\nIndex value of no 34 is:")
print a.index(34)

#Pop  operation
print("\n\n****Pop operation perform****")
print("Remove last element\nthat is")
print a.pop()
print ("\nNow List is: ");
print (a);


#Append Operation
print("\n\n****Append Operation****")
a.append(31)
print("insert value 31 end of list")

print ("\nNow List is: ");
print (a);


#Remove Operation
print("\n\n****Remove Operation****")
a.remove(77)
print("No 77 is removed in the list")
print ("\nNow List is: ");
print (a);

#Insert Operation
print("\n\n****Insert operation****")
a.insert(a.index(8),24)
print("Insert value 24 in value 8 position")
print ("\nNow List is: ");
print (a);
