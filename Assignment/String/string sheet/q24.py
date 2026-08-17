'''
4Check if all characters in a string are unique.
 S1 = "abc", S2 = "abca" 
S1: True, S2: False
'''
s1=input("Enter the string")
s2=input("Enter the string")
for i in s1:
    c=s1.count(i)
    if c==1:
        continue
    else:
        print("False")
        break
else:
    print("True")
for i in s2:
    c=s2.count(i)
    if c==1:
        continue
    else:
        print("False")
        break
else:
    print("True")