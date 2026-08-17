'''
52Remove all special characters. 
S = "a!@b#c" 
"abc"
'''
s=input("Enter string")
res=""
for i in s:
    if 'a'<=i<='z' or 'A'<=i<='Z':
        res=res+i
    else:
        continue

print(res)