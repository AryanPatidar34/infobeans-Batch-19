'''
49Replace all consonants with ''.
 S = "apple"
 "ae"
'''

s=input("Enter string")
con=""
for ch in s:
    if ch in 'aeiou':
        con+=ch
print(con)