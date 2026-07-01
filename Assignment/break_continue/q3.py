'''

3. Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35
'''


m = int(input("Enter the number"))
n = int(input("Enter the number"))
'''
for i in range(m+1,n):
    if i%5==0:
        if i%2!=0:
            print(i)
    else:
        continue
'''

while m<n:
    m=m+1
    if m%5==0:
        if m%2!=0:
            print(m)
    else:
        continue
       