'''
Count total occurrences of a character.
 S = "programming", 
Char = 'g'
 2

s=input("Enter the string :")
ch=input("Enter the character :")
c=0
for i in s:
    if i==ch:
        c+=1
    else:
        continue

print(c)
'''
s=input("Enter the string :")
ch=input("Enter the character :")
c=s.count(ch)
print(c)

    