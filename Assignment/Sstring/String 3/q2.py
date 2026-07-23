'''
2.  Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST
'''

n=input("Enter your name")
count=1
x=0
rev=""
for ch in n:
    if count==1:
        if ch>='a' and ch<='z':
            rev=rev+chr(ord(ch)-32)
            count=0
        else:
            pass
    elif x==1:
        rev=rev+chr(ord(ch)-32)
        x=0

    elif ch==" ":
        x=1
    
print(rev)