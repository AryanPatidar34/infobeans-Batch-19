'''
19Find the highest frequency character. 
S = "abracadabra" 
a' 

'''
s=input("Enter the string")
hfreq=0
for i in s:
   c=s.count(i)
   if c>hfreq:
       hfre=c
   
print(hfreq)
       