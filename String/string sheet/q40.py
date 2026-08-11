'''
40Search all occurrences of a word.
 S = "a b a b", 
Word='b' 2, 6 (start indices)
'''
s=input("Enter the string")
char=input("Enter char")
for i in range(len(s)):
    if s[i]==char:
        print(i,end=",")