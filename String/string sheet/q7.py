'''
7
Convert a string to lowercase. 
S = "HELLO"
 "hello"

'''
s=input("Enter the string")
res=""
for i in s:
     if 'A'<=i<='Z':
         res+=chr(ord(i)+32)
         
     else: 
         res+=i
     
print(res)
'''
s=input("Enter string")
i=0
res=""
while i<len(s):
    ch=s[i]
    if 'A'<=ch<='Z':
         res+=chr(ord(ch)+32)
         #print(res)
    else:
         res+=ch
    i+=1

print(res)
'''