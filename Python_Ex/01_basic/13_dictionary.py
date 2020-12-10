"""This is my dictionary concept program"""

#key,value=>dictionary

details={"name":"Manimaran","No":24}
print "\n\n"
print "Print the Full Dictionary elements"
print details


print "\n\n"

print "Print the particular key elements"
print details["name"]


#Collection of dictionary
student_det={4001:{"name":"Abu","No":01},4002:{"name":"Anand","No":02}}

print "\n\n"
print student_det

print "\n\n"
print student_det[4001]

print "\n\n"
for key,value in student_det.iteritems():
    print key,value

print "\n\n"
for key,value in student_det.iteritems():
    print key,value["name"]


print "\n\n"
for key,value in student_det[4001].iteritems():
    print key,value

print "\n"
print "Has_key check:"
print student_det.has_key(4001)
print student_det.has_key(4003)
print "\n"

