'''
73Find the longest palindromic substring. S = "babad" "bab" (or "aba")
'''
s=input("Enter string")
lar=""
for i in range(len(s)):
    ch=s[i]
    cs=ch
    for j in range(i+1,len(s)):
        cs=cs+s[j]
        temp=cs
        rev=cs[::-1]
        if temp==rev:
            if len(cs)>len(lar):
                lar=cs
print(lar)