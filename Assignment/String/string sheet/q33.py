'''
Find the longest word. 
S = "find the longest word"
 "longest"
'''

n=input("Enter string")
n=n.split()
i=0
larl=len(n[i])
lar=n[i]
while i<len(n):
    ch=n[i]
    if len(ch)>larl:
        lar=ch
        
    i+=1
print(lar)