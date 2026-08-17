'''
Remove occurrences of a character.
 S = "banana", Char = 'a', 
Remove All "bnn"
'''
s=input("Enter the string :")
ch=input("Enter the character :")
res=""
for i in s:
    if i!=ch:
        res+=i
    else:
         continue

print(res)