'''
4. Numbers Divisible by 3 Between Two Numbers
A school is organizing a quiz competition. Only students whose roll numbers are divisible by 3 are selected for the first round. The teacher enters a roll number range and wants the system to display eligible roll numbers.
Write a program to display numbers divisible by 3 between two given numbers using loops.

Input:
10 25

Output:
12 15 18 21 24'''

#using while loop
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))

while a<=b:
     if a%3==0:
        print(a)
     a=a+1

#using for loop
'''for i in range(a,b+1):
    if a%3==0:
        print(a) 
    a+=1'''
        


