'''

8. Count Multiples of 5 Between Two Numbers
A supermarket gives coupons to customers whose token numbers are multiples of 5. The manager enters a token range and wants to know how many eligible token numbers exist.
Write a program to count numbers divisible by 5 between two given numbers using loops.

Input:
1 20

Output:
Count = 4'''

n = int(input("Enter the number"))
x = int(input("Enter the number"))
count=0
'''
for i in range(1,x+1):
    if i%5==0:
        count=count+1
    i+=1
print(count)'''


while n<=x:
    if n%5==0:
        count=count+1
    n=n+1

print("Count:",count)