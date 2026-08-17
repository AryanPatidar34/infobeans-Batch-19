'''
54Replace all duplicate characters with '$'.
 S = "hello"
 "he$lo"
'''
s=input("Enter string")
res=""
temp=""
for i in s:
   if i not in temp: 
       temp+=i
       if s.count(i)>1:
           res+='$'
       else:
           res+=i
        
   else:
        res+=i
   
   
        
print(res)