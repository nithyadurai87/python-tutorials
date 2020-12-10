"""File Operation """

#write a file
fob=open('new.txt','w')
fob.write("i am manimaran")
fob.close()

#read the file
fob=open('new.txt','r')
print fob.read()
