'''
NOTE: in all the programs read length and array elements from user
=====================================================================
1.Student Marks Management
Create a program to store student marks in a List and perform operations.

Requirements:

Add student marks into a List
Display all marks
Find highest and lowest marks
Count students who scored above 75

Test Cases:

Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3
'''
n=int(input("Enter total students size"))
marks=[]
for i in range(n):
    x=int(input("Enter the number"))
    marks.append(x)
print("marks :",marks)
high=marks[0]
low=marks[0]
c=0
for i in marks:
    if i>high:
        high=i
    if i<low:
        low=i
    if i>75:
        c+=1

print("highest : ",high)
print("lowest : ",low)
print("Above 75 : ",c)
