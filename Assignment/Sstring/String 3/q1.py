'''
1.  Bank Customer Account Privacy System

A national bank is developing a secure customer portal where account
numbers should not be displayed completely on the screen. For security
reasons, the system should hide all digits except the last four digits
before showing them to users.

Conditions: - Display only the last 4 digits - Replace all previous
characters with *

Input: Enter account number: 123456789012

Output: Masked Account: ****9012
'''

n=input("Enter account number")
i=0
while i<len(n):
    ch=n[i]
    if len(n)-i<=4:
        print(ch,end="")
    else:
       print("*",end="")
    i+=1
    