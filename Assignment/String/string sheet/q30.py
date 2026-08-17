'''
Replace a word with another word. 
S = "old data", Old="old", New="new"
 "new data"
'''
s=input("Enter the string")
n=s.split()
res=""
i=0
while i<len(n):
    ch=n[i]
    if ch=="old":
        res+="new"+" "
    else:
        res+=ch+" "
    i+=1
print(res)