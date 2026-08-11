'''
4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31'''


import math
n=int(input("Enter the number"))
n=n+1

while True:
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            break
    else:
        print("next prime : ",n)
        break
    n=n+1
    
        