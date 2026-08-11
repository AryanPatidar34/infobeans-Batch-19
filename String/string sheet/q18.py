'''
Replace occurrences of a character.
 S = "apple", Old='p', New='x' 
"axxle"
'''
s=input("Enter the string :")
old=input("Enter the character :")
new=input("Enter the character :")
res=""
for i in s:
   if i==old:
       res+=new
   else:
       res+=i

print(res)