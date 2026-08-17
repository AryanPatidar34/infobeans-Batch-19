'''
41Check if a string contains a substring (without using contains()). 
S1 = "Hello", Sub = "ell" 
TRUE
'''

s=input("Enter string")
w=input("Enter sub")
print(w in s)
'''
for i in range(len(s)):
    ch=s[i]
    print(ch)
    cs=ch
    for j in range(i+1,len(s)):
        cs=cs+s[j]
        print(cs)
'''
               
