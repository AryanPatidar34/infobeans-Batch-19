'''
7. Power of a Number
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32
'''


n =int(input("Enter the number"))
x =int(input("Enter the number"))
sum=0
for i in range(1,x+1):
     if i==x:
         sum = sum+n**x
     i=i+1
print(sum)
    
