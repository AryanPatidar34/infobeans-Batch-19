'''
6.

A security system logs employee entry IDs during a day.

Only prime-numbered IDs are considered valid VIP entries.

Tasks:

Extract all prime IDs from the list
Find the sum of prime IDs
Find the maximum prime ID
Count how many prime entries exist

Input:
A list of integers (may contain duplicates and non-prime numbers)

Example 1

Input:
[12, 5, 7, 9, 11, 14, 17]

Output:
Prime IDs = [5, 7, 11, 17]
Sum = 40
Max = 17
Count = 4

Example 2

Input:
[4, 6, 8, 10]

Output:
Prime IDs = []
Sum = 0
Max = -1
Count = 0
'''
import math
n=list(map(int,input("Enter elements").split()))
prime=[]
lar=0
c=0
for i in n:
    if i==1:
        continue
    else:
        for j in range(2,i//2):
            if i%j==0:
                break
        else:
            prime.append(i)
            c+=1
            if i>lar:
                lar=i
sum=sum(prime) 
         
print("Prime IDs :",prime)
print("Sum",sum)
print("Max :",lar)
print("Count",c)