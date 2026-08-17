'''
n=input("Enter the string")
words=n.split()
for i in range(0,len(words)):
    w=words[i]
    rev=""
    for j in range(len(w)-1,-1,-1):
        rev=rev+w[j]
     
    print(rev,end=" ")
'''

n=input("Enter the string")
words=n.split()
for i in range(0,len(words)):
    w=words[i]
    rev=""
    rev=w[::-1]
    print(rev,end=" ")



