"""*10. Even Numbers Between Two Numbers*
A teacher wants to assign only even roll numbers for a special activity. The system should display all even numbers between two given numbers.
Write a program to *display all even numbers between two numbers using loops*.

Input: 10, 20
Output: 10 12 14 16 18 20"""

# using for loop
'''
a,b=map(int,input("Enter the number").split())
for i in range(a,b+1,2):
    print(i,end=" ")'''

#using while loop
a,b=map(int,input("Enter the numbers").split())
i=a
while i<=b:
          print(i,end=" ")
          i+=2
