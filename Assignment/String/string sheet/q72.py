'''
72Print all substrings of length n. S = "abc", n = 2 "ab, bc"
'''
s=input("Enter the string")
n=int(input("Enter length"))
for i in range(n):
    ch=s[i]
    cs=ch
    for j in range(i+1,n+1):
        cs=cs+s[j]
        if len(cs)==n:
            print(cs)