'''
Remove duplicate words. 
S = "the cat and the dog"
 "the cat and dog"
'''
s=input("Enter the string")
n=s.split()
res=""
i=0
while i<len(n):
    ch=n[i]
    if ch not in res:
        res+=ch+" "
    i+=1

print(res)