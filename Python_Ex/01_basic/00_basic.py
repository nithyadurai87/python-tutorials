"""basic elements"""

print "Basic declaration"
a=5
b=7
c=a+b
print a
print b
print c
print a-b

print "List elements"
one=[1,2,3]
two=[5,6,7]
one.extend(two)
print one

print "Boolean operation"
print 9>3
print one is two

print "Multiple parameters"
def profile(name,*ages):
    print name
    print ages

profile('mani',23,24,25)


print "Tuples as Parameters"
def ex(a,b,c):
    return(a+b*c)

m=(2,3,4)
print ex(*m)


print "Tuples as Parameters 2"
def ex2(**this):
    print this

tup={'mani':21,'kavi':22}
ex2(**tup)



print "Parameters Type"
def pro(first,last,*ages,**items):
    print('%s' '%s' %(first,last))
    print ages
    print items

pro('mani','maran',20,21,apple=20,mango=45)



print "string connect another string"
bad="Mani hate %s and %s"
fill=('fb','windows')
print bad %fill


