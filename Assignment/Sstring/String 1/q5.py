'''
5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password
'''

n=input("Enter the password")
upper=0
digit=0
special=0
space=0
if len(n)<=8 and len(n)>=15 :
     print("invalid password1")
else:
    for ch in n:
        if ch>='a' and ch<='z':
            print("invalid password")
            break
        else:
            if ch>='A'and ch<='Z':
                upper=1
             
            elif ch>='0' and ch <='9':
                digit+=1
             
            elif ch in '@#$&*':
                special=1
             
            elif ch==" ":
                space+=1
            
        if upper==1 and digit>=2 and special>=1 and space==0:
            print("secure password")
        else:
            print("insecure password2")