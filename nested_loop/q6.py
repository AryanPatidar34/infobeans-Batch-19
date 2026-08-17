'''
6.
Palindrome Number Range Checker

A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200

Output:
Palindrome Numbers are:
101
111
121
131
141
151
161
171
181
191'''


x=int(input("Enter the number"))
y=int(input("Enter the number"))

for i in range(x,y+1):
    temp=i
    num=i
    rev=0
    while num>0:
        d=num%10
        rev=rev*10+d
        num=num//10
    if rev==temp:
       print(temp)
        
        