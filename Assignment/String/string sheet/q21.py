'''
21Find the first non-repeating character.
 S = "aabbcde" 
c'
'''
s=input("enter the string")
for i in s:
    c=s.count(i)
    if c==1:
        print(i)
        break