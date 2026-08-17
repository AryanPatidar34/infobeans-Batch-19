'''
5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3

'''
import math
n=int(input("Enter the number"))
n=n+1
while True:
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            break
    else:
        print("next prime :",n)
        break
    n=n+1