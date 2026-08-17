'''
6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2
'''

n=int(input("Enter the number"))
i=1
count=0
sf=9
while i<=n:
    if n%i==0:
        count+=1
        if i<sf and i>1:
            sf=i
                    
    i=i+1
if count>2:
    print("composite number")
print("Fctor count",count)
print("smallest factor",sf)
    
        