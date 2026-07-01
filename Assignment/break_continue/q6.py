'''

6. Automorphic Number Checker

A digital security company designs smart lockers that open only for special self-matching numeric codes. When a user enters a number, the system squares the number and checks whether the result ends with the same digits as the original code. If yes, the locker grants access.

An automorphic number is a number whose square ends with the same number.

Example:
25² = 625

Write a program using loops to check whether the entered number is an Automorphic number.

Input:
25

Output:
Automorphic Number

'''
n=int(input("Enter the number"))
sq=n**2
count=0
l=len(str(n))
for i in range(l):
    d=n%10
    d1=sq%10
    if d==d1:
        count=count+1
    n=n//10
    sq=sq//10 
          
     
if count==l:
    print("atmorphic number")
else:
    print("not atmorphic number")