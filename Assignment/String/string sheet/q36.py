'''
Reverse order of words. 
S = "one two three" 
"three two one"
'''

s=input("Enter string").split()
i=-1
res=""
while i>=-len(s):
     res+=" "+s[i]
     i-=1
print(res)
    