'''
8.
Trimorphic Number Analyzer

A coding system checks cube-based patterns.

A Trimorphic Number:
Cube of number ends with the same number.

Example:
4³ = 64

Write a program to check Trimorphic Number.

Input:
4

Output:
Trimorphic Number'''


n=int(input("Enter the number"))
c=n**3
while n>0:
    if n%10!=c%10:
        print("not a trinorphic")
        break
    n=n//10
    c=c//10
else:
    print("Trimorphic number")
    
    