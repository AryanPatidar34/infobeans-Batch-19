'''
8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime'''

import math
n=int(input("Enter the number"))
lar=0
min=9
sum=0
while n>0:
    d=n%10
    if d>lar:
        lar=d
    elif d<min:
        min=d
    n=n//10
sum=lar+min
print("Largest :",lar)
print("Smallest :",min)
print("Sum :",sum)
if sum<=1:
    print("not prime")
i=2
while i<math.sqrt(sum):
    if sum%i==0:
        print("not a prime number")
        break
    i=i+1
else:
    print("Prime Number")
    