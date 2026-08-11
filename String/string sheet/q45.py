'''
45Check whether a string starts/ends with another string.
 S = "apple pie", Prefix = "apple", Suffix = "pie"
 Start: True, End: True
'''

s1=input("enter string1")
pre=input("enter prefix")
suf=input("enter suffix")
print(s1.startswith(pre))
print(s1.endswith(suf))