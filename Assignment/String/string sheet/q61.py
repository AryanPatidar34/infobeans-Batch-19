'''
61Count total alphabets, digits, and special characters. 
S = "a1b!c2" 
Alphabets: 3, Digits: 2, Special: 1
'''
s=input("Enter the string")
ac=0
d=0
sp=0
for i in s:
    if 'a'<=i<='z':
        ac+=1
    elif i in '0123456789':
        d+=1
    else:
        sp+=1

print("Alphabet :",ac,"Digits :",d,"Special :",sp)