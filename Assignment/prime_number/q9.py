'''
9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime
'''
import math
n=int(input("Enter the number"))
ecount=0
ocount=0

while n>0:
    d=n%10
    if n%2==0:
        ecount=ecount+1
    else:
        ocount=ocount+1
    n=n//10

diff=ecount-ocount


if diff<=1:
    print("not prime")
else:
    for i in range(2,int(math.sqrt(diff))):
        if n%i==0:
           print("not a prime number")
           break
    
    else:
        print("prime number")
    
print("Even Digit :",ecount)
print("Odd Digit :",ocount)
print("Difference :",diff)


