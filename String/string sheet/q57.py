'''
57Merge two strings alternatively (char by char).
 S1 = "ABC", S2 = "def"
 "AdBeCf"
'''
s1=input("Enter string 1")
s2=input("Enter string 2")
res=""      

less=min(len(s1),len(s2))
for j in range(less):
     res+=s1[j]+s2[j]
if len(s1)>len(s2):
    res=res+s1[len(s2):]
else:
    res=res+s2[len(s1):]
print(res)
        
    