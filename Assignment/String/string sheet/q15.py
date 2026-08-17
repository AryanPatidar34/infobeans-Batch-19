'''
Find the last occurrence of a character. 
S = "banana", 
Char = 'a' 
5 (index)
'''

s=input("Enter the string :")
c=input("Enter the character :")
i=len(s)-1
while i>=0:
    ch=s[i]
    if ch==c:
        print(i)
        break
    i-=1