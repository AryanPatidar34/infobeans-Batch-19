'''
Find the shortest word.
 S = "find the shortest word" 
"the"
'''
n=input("Enter string")
n=n.split()
i=0
min=n[0]
word=""
while i<len(n):
    if len(n[i])<len(min):
        word=n[i]
    i+=1
print(word)