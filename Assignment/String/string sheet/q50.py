'''
50Remove all digits.
 S = "a1b2c3"
 "abc"
'''

s=input("Enter string")
res=""
for i in s:
    if i in '0123456789':
        continue
    else:
        res=res+i

print(res)