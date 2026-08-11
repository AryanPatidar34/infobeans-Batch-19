'''
Compare two strings ignoring case.
 S1 = "Test", S2 = "test" 
Equal (or 0)
'''
s1=input("Enter the string")
s2=input("Enter the string")
if s1.lower()==s2.lower():
    print("equal")
else:
    print("not equal")