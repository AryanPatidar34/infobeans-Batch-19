'''
2. Factorial of a Number
In project scheduling, tasks are dependent on previous tasks, and the total number of ways to arrange them is calculated using factorial. Factorial of a number n is the product of all numbers from 1 to n.
Write a program to calculate the *factorial of a given number using loops*.

Input: n = 5
Output: Total Ways = 120
'''

#using for loop
'''
n= int(input("Enter the number"))
fact=1
for i in range(n,0,-1):
    fact = fact*i
print("Total ways:",fact)



#using while loop

n= int(input("Enter the number"))
fact = 1
i=n
while n>=1:
      fact=fact*i
      i-=1
print("Total ways:",fact)'''


# second type using while 
n= int(input("Enter the number"))
fact=1
i=1
while i<=n:
      fact=fact*i
      i+=1
print("Total ways",fact)
