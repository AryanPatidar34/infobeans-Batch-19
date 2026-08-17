'''
6.

Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching
'''
x=input("Enter string 1").lower()
y=input("Enter string 2").lower()
s=1
for ch in x:
    if ch==" ":
        pass
    else:
        c1=0
        c2=0
        j=0
        while j<len(x):
            if x[j]==ch:
                c1+=1
            j+=1
        j=0
        while j<len(y):
            if y[j]==ch:
                c2+=1
            j+=1
        if c1!=c2:
            s=0
            break

if s==1:
    print("both product are matching ")
else:
    print("both product are not match")
        