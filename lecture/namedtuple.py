from collections import namedtuple
Student=namedtuple("Student",["rollno","name","marks"])
n=int(input("Enter number of student"))
student=[]
for i in range(n):
    print("Enter student details")
    r=int(input("Enter roll no."))
    name=input("Enter name")
    m=int(input("Enter marks"))
    s=Student(r,name,m)
    student.append(s)
for i in student:
    print("student detail")
    print(i.rollno,i.name,i.marks)

