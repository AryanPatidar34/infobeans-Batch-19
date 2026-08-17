'''
65Count palindromic substrings. 
S = "aaa" 
6 (a, a, a, aa, aa, aaa)
'''
s=input("Enter string")
c=0
for i in range(len(s)):
    ch=s[i]
    print(ch)
    c+=1
    
            
    cs=ch
    for j in range(i+1,len(s)):
        cs=cs+s[j]
        temp1=cs
        rev=cs[::-1]
        if temp1==rev:
            c+=1
        print(cs)

print(c)