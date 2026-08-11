'''
Print all characters that occur exactly twice. 
S = "aabbcdee" 
b', 'e'
'''
s=input("Enter the string")
for i in s:
    c=s.count(s)
    if c==2:
        print(i,end=" ")