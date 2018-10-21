student_details = []

def get_stu_det():
    name = raw_input("Enter your name: ")
    reg_no = input("Enter your reg_no: ")
    dept = raw_input("Enter your dept")

    student_details.append(name)
    student_details.append(reg_no)
    student_details.append(dept)

n=input("Enter no of student_details: ")

for i in range(0,n):
    get_stu_det()

for det in student_details:
    print det
