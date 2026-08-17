'''
44Check if two strings are anagrams. 
S1 = "listen", 
S2 = "silent" 
TRUE
'''
s1=input("enter string1")
s2=input("enter string2")
if len(s1)!=len(s2):
    print("not anagram")
else:
    for ch in s1:
        if ch not in s2:
             print("not anagram")
             break
    else:
        print("anagram")