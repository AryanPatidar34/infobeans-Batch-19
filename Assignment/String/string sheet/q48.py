'''
48Remove all vowels.
 S = "aeiou XYZ"
 " XYZ"
'''
s=input("Enter string")
res=""
for vol in s:
    if vol in 'aeoiu':
        continue
    else:
        res=res+vol
print(res)
