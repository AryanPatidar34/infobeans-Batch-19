'''
4.

Find All Characters with Maximum Frequency
Website Traffic Analysis System

A web analytics company tracks user activity symbols in server logs.

The company wants to identify all characters having the maximum frequency in the given string.

Input:
aabbbccddd
Output:
b d

'''

n=input("Enter your string")
i=0
temp=""
larc=0
lar=""
while i<len(n):
    ch=n[i]
    if ch not in temp:
        temp+=ch
        c=n.count(ch)
        if c>larc:
            larc=c
            lar=ch
        elif c==larc:
            larc=c
            lar+=" "+ch
    i+=1

print(lar)
