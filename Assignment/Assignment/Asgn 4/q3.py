"""
Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2
"""
sub = int(input("Enter total sunject : "))
m1 = int(input("subject 1 : "))
m2 = int(input("subject 2 : "))
m3 = int(input("subject 3 : "))
m4 = int(input("subject 4 : "))
m5 = int(input("subject 5 : "))
sum  =m1+m2+m3+m4+m5
print("Total :" , (sum))
total_marks = sub*100
Avg = sum/sub
print("Average :",(Avg))
per = sum*100/total_marks
print("Percentage :",(per))