'''
38Reverse words without split().
 S = "a b c"
 "c b a"
'''

s=input("Enter the string")
i=-1
res=""
while i>=-len(s):
    res+=s[i]
    i-=1

print(res)