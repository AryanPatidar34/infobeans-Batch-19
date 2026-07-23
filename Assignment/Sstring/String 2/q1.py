'''
1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username
'''
n=input("Enter your Email")
count=0
space=0
allow=0

if len(n)<5 and len(n)>12:
    print("invalid")
    
   
else:
    for ch in n:
         if not((ch>='a' and ch<='z') or(ch>='A' and ch<='Z')):
             print("invalid 1")
             break
         else:
             if ch in '0123456789' or ch=="_":
                 count=1
             elif ch==" ":
                 space=1
             else:
                 print("invalid 2")
                 break
         if count>=1 and space==0 and allow==1:
             print("valid")
         else:
             print("invalid")
'''


#using while loop
n=input("Enter your Email")
count=0
space=0
allow=0

if len(n)<5 and len(n)>12:
    print("invalid")


i=0
while i<=len(n)-1:
       ch=n[i]
       if not((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
           print("invalid 1")
           break
       
       else:
           if ch==" ":
                space+=1
           elif ch in '0123456789' or ch=='_':
                allow=1
           else:
                print("invalid 2")
                break
           
       i+=1
       if count>=1 and space==0 and allow==1:
                print("valid")
       else:
            print("invalid3")
'''                
        