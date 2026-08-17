'''
Find the first occurrence of a character. 
S = "banana", 
Char = 'a' 
1 (index)
'''

s=input("Enter the string :")
c=input("Enter the character :")
for i in range(0,len(s)):
    ch=s[i]
    if ch==c:
         print(i)
         break


