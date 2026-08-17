'''
7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number
'''

n=input("Enter the string")
d=0
count=0
if len(n)<10 or len(n)>10:
    print("invalid l")
    
else:
    i=0
    while i<4:
        ch=n[i]
        if ch>='A' and ch<='Z' or ch>='a' and ch<='z':
            count+=1
        elif ch in '1234567890':
            d+=1 
  
        i+=1
    if count==2 and d==2:
        print("valid")
    else:
        print("invalid")
         