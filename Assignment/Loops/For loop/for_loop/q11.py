'''*11. Count Occurrence of a Digit*
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to *count how many times a given digit appears in a number using loops*.

Input: Number = 122312, Digit = 2
Output: 3'''

#using for loop
'''
n= int(input("Enter the number"))
digit = int(input("Enter the digit"))
count=0
for i in range(len(str(n))):
    rem=n%10
    if rem==digit:
        count+=1
    n=n//10
print(count)
'''

#using while loop
n= int(input("Enter the number"))
digit = int(input("Enter the digit"))
count=0

while n>0:
      rem=n%10
      if rem==digit:
          count+=1
      n=n//10
print(count)