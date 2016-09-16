def names(list1):
    list2 = []
    for i in list1:
	    j = i.find(' ')
	    i = i[:j+2]
	    list2.append(i)
    print list2

names(['Nithya Durai','Vijaya Kishor','Anitha Raj'])	