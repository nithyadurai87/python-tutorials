"""This program -join,split,strip"""

#string
s="Mani is \n good \n boy not bad"
print "\nString value=",s
print "\n"

#split the string
s1=s.split()
print "Spliting the string=",s1
print "\nSpliting \\n the string=",s.split("\n")

name="a-b-c"
print "\n",name
print "\nSpliting ""-"" the string=",name.split("-")


#join:
s="-"
a=["a","b","c"]
print "\ns=",s
print "\na=",a

print "\n Join of a and s=",s.join(a)



#strip
str1="           Mani   maran "
print "\nstring=",str1

print "\nstring striped=",str1.strip()



