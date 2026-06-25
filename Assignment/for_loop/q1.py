"""
Note: Read all the values from user. Use loops wherever required.
NOTE: complete all programs using both the loops

---

1. Sum of First N Natural Numbers
A teacher wants to reward students by giving points daily. On day 1, a student gets 1 point, day 2 → 2 points, and so on. This follows a natural number sequence.
Write a program to calculate the *total points earned after n days* by summing all natural numbers up to n using loops.

Input: n = 10
Output: Total Points = 55
"""


# using for loop
'''n= int(input("Enter the number"))
points =0
for i in range(1,n+1):
     points= points+i

print("Total points = ",points)'''


# using while loop

n= int(input("Enter the number"))
points=0

i=1
while i<=n:
      points=points+i
      i+=1

print("Total points=",points)