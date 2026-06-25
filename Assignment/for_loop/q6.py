'''
6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong
'''
'''
#using for loop
n = int(input("Enter the number"))
sum=0
temp=n
for i in range(len(str(n))): 
    rev =0
    rev = n%10
    sum += rev**3
    n= n//10

if temp==sum:
    print("Armstrong")
else:
    print("not Armstrong")'''


#using while loop
n = int(input("Enter the number"))
sum=0
temp=n
while n>0:
      rev=0
      rev=n%10
      sum+=rev**3
      n=n//10
if temp==sum:
    print("Armstrong")
else:
    print("not Armstrong")

    