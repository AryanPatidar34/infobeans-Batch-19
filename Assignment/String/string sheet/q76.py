'''
76Find the longest common suffix among strings. 
Strings = ["baking", "making", "taking"] 
"aking"
'''
s=input("Enter string")
words=s.split()
small=s
for i in words:
    if len(i)<len(small):
        small=i
#print(small)
i=0
while i<len(small):
    check=small[i:]
    k=0
    c=0
    while k<len(words):
        if words[k].endswith(check):
            c+=1    
        k+=1
    if c==len(words):
        print(check)
        break
    i+=1
else:
    print("no suffix found")

