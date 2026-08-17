'''
5. Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www - Must end with .com

Input: Enter website: www.amazon.com

Output: Valid Website
'''

n=input("Enter your website")
        
rev=" "
if n[0]==" ":
    print("remove space first")
    
else:
    if n[0]=='w' and n[1]=='w' and n[2]=='w' and n[3]=='.':
        i=4
        while i<len(n)-4:
            ch=n[i]
            if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
                rev=rev+ch
            else:
                print("invalid...")
                break
                
            i+=1
        else:
            if rev!=" ":
                if n[-1]=='m' and n[-2]=='o' and n[-3]=='c' and n[-4]=='.':
                    print("valid")
                else:
                    print("invalid 1")
            else:
                 print("invalid 2")
    else:
         print("invalid 3 ")
        
    