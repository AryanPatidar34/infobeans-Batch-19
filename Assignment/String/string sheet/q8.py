'''
8
Toggle the case of each character. 
S = "MiXED" 
"mIxeD"
'''
'''
s=input("Enter the string")
res=""
for i in s:
    if 'A'<=i<='Z':
         res+=chr(ord(i)+32)
    else:
        res+=chr(ord(i)-32)
print(res)
'''
s=input("Enter the string")
res=""
for i in s:
    if 'A'<=i<='Z':
         res+=i.lower()
    else:
        res+=i.upper()
print(res)

