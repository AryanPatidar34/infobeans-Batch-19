'''
51Extract only digits.
 S = "a1b2c3" 
"123"
'''
s=input("Enter string")
res=""
for i in s:
    if i in '0123456789':
        res=res+i
    else:
        continue

print(res)