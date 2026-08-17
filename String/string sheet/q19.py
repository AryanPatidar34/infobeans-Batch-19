'''
19Find the highest frequency character. 
S = "abracadabra" 
a' 

'''
s=input("Enter the string")
freq=""
count=0
for i in s:
   c=s.count(i)
   if c>count:
       count=c
       freq=i
   
print(freq)
       