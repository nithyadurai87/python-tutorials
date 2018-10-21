"""For loop using"""

student_details=["Mani","prem","kumar"]


#method 1
print("\n****Normal for loop****")
for i in student_details:
    print i


#method 2
print("\n\n\n****Range using:****")
for i in range(0,2):
    print student_details[i]

#method 3
print("\n\n\n****Range using with len fn(dynamicaly assign end value)****")
for i in range(0,len(student_details)):
    print student_details[i]

#method 4
print("\n\n\n****Using list name in for loop****")
for i in student_details[0:2]:
    print i
