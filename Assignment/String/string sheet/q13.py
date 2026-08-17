'''
Get the Unicode code point before index.
 S = "Hello", Index = 1 
72 (Unicode for 'H')
'''

s=input("Enter string")
index=int(input("Enter index"))
res=ord(s[index])
print(res)

