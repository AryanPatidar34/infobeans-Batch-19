'''
47Check for substring using concatenation trick. 
S1="CDAB", S2="ABCD"
 True (S1 is in S2+S2)
'''

s1=input("Enter string")
s2=input("Enter string")
for ch in s1:
    if ch not in s2:
         print("False")
         break
else:
    print("True")
   