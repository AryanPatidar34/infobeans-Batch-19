'''
=====================================================================
QUESTION 1: EMPLOYEE SALARY ANALYSIS
====================================

A company wants to store employee details and generate salary reports using NamedTuple.

Fields:
emp_id, emp_name, department, salary

Requirements:

1. Read N employee details from the user and store them in a list of NamedTuples.

---

2. Display all employee details.

---

3. Find and display the employee with the highest salary.

---

4. Find and display the employee with the lowest salary.

---

5. Calculate and display the average salary of all employees.

---

6. Accept a department name from the user and display all employees belonging to that department.

---

Test Case:

Input:
Enter number of employees: 4

101 Rahul IT 50000
102 Priya HR 45000
103 Amit IT 70000
104 Neha Finance 60000

Enter department: IT

Expected Output:
Highest Salary Employee:
103 Amit IT 70000

Lowest Salary Employee:
102 Priya HR 45000

Average Salary:
56250.0

Employees in IT Department:
101 Rahul IT 50000
103 Amit IT 70000
'''

from collections import namedtuple
Employee=namedtuple("basic",["emp_id","emp_name","department","salary"])
n=int(input("Enter size of employees"))
arr=[]
for i in range(n):
    id=int(input("Enter id : "))
    name=input("Enter name : ")
    dept=input("Enter department : ")
    sal=int(input("Enter salary"))
    arr.append(Employee(id,name,dept,sal))
print(arr)
dep=input("Enter Department : ")
high=arr[0]
low=arr[0]
sum=0
for i in arr:
    sum+=i.salary
    if i.salary<low.salary:
            low=i

    if i.department==dep:
        if i.salary>high.salary:
            high=i
print()                       
print("Highest Salary Employee:",high.emp_id,high.emp_name,high.department,high.salary)
print()
print("Lowest Salary Employee:",low.emp_id,low.emp_name,low.department,low.salary)
print()
print("Average salary :",sum/n)
for i in arr:
    if i.department == dep:
        print("Employee in IT Department :")
        print(i.emp_id, i.emp_name, i.department, i.salary)
     


