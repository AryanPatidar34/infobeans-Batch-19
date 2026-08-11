'''
58Rotate characters by 2 positions to the left. 
S = "abcde"
 "cdeab"
'''

s=input("Enter string")
temp=""
res=""
for i in range(2):
    temp+=s[i]
for i in range(2,len(s)):
    res+=s[i]
temp=res+temp
print(temp)
    