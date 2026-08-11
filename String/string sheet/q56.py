'''
56
Reverse only consonants.
 S = "apple" 
"eplpa"
'''
s=input("Enter string")
con=""
res=""
for i in s:
    if i not in 'aeiou':
        con+=i
rev=con[::-1]
k=0
for i in s:
    if i not in 'aeiou':
        res+=rev[k]
        k+=1
    else:
        res+=i

print(res)