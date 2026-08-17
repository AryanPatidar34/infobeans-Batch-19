'''
71Print all substrings. S = "abc" "a, b, c, ab, bc, abc"

s=input("Enter the string")
for i in range(len(s)):
    ch=s[i]
    print(ch)
    cs=ch
    for j in range(i+1,len(s)):
        cs=cs+s[j]
        print(cs)
'''
s=input("Enter the string")
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        print(s[i:j],end=" ")

    
