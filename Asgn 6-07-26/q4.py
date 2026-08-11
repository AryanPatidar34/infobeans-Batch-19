'''
4.Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number'''


n=int(input("Enter the number"))
sum=0
mul=1
while n>0:
    d=n%10
    sum=sum+d
    mul=mul*d
    n=n//10
if mul==sum:
    print("spy number")
else:
    print("not a spy number")