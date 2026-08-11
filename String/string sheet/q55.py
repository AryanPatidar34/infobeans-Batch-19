'''
Reverse only vowels.
 S = "hello" 
"holle"
'''
s=input("Enter the string")
vol=""
res=""
for i in s:
    if i in 'aeoiu':
        vol+=i
rev=vol[::-1]
k=0
for i in s:
    if i in 'aeiou':
        res+=rev[k]
        k+=1
    else:
        res+=i

print(res)


    
