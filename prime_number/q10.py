'''
10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime'''

import math
n=int(input("Enter the number"))
sum=0
count=0
min=9
while n>0:
    d=n%10
    if d==0:
        count+=1
    sum=sum+d
    if d<9:
       min=d
    result=sum*min
    n=n//10
    

print("Zero Count :",count)
print("sum :",sum)
print("smallest Digit",min)
print("final result ",result)
if result<=1:
    print("not prime")
else:
    for i in range(2,int(math.sqrt(result))):
        if n%i==0:
           print("not a prime number")
           break
    
    else:
        print("prime number")

