'''
67Count how many times a substring appears.
 S = "abab", Sub = "ab" 
2
'''
s=input("Enter string")
sub=input("Enter substring")
c=0
for i in range(len(s)):
    ch=s[i]
    cs=ch
    for j in range(i+1,len(s)):
        cs=cs+s[j]
        if cs==sub:
            c+=1
print(c)