'''
0Find the lowest frequency character. 
S = "aabbcde" 
c', 'd', 'e' (any one or all)

'''
s=input("Enter the string")
freq=""
count=9

for i in s:
   c=s.count(i)
   if c<count:
       count=c
       freq=i+" "
   elif c==1:
       freq+=i+" "

print(freq)
