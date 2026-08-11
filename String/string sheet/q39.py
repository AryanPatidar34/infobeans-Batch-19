'''
39Search all occurrences of a character. 
S = "banana", 
Char='a' 1, 3, 5 (indices)
'''

s=input("Enter the string")
char=input("Enter char")
for i in range(len(s)):
    if s[i]==char:
        print(i,end=",")
