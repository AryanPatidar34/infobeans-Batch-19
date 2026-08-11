'''
43Check if two strings are rotations of each other.
 S1 = "abcde", S2 = "cdeab" 
TRUE
'''

s1=input("enter string1")
s2=input("enter string2")
if len(s1)!=len(s2):
    print("Flase")
else:
    for ch in s1:
        if ch not in s2:
             print("False")
             break
    else:
        print("True")
        
         