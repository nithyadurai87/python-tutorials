list1 = ['Nithya Duraisamy','Vijaya Kandasamy','Anitha Rajagopal']
list2 = []
for i in list1:
	j = i.find(' ')
	i = i[:j+2]
	list2.append(i)
print list2