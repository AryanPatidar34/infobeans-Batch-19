'''
78Find the longest mirror-image substring at both ends.
 S = "aabccbaa" 
"aab"
'''

s=input("Enter string")
i=0
j=len(s)-1
res=""
for i in range(len(s)//2):
   if s[i]==s[j]:
      res+=s[i]
      j-=1
   else:
       break 
print(res)

