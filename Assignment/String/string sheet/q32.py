'''
Count frequency of each word. 
S = "apple banana apple" 
apple: 2, banana: 1
'''

n=input("Enter string")
word=n.split()
vis=""
i=0
while i<len(word):
    ch=word[i]
    if ch not in vis:
        vis+=ch
        c=0
        for j in range(len(word)):
            if ch==word[j]:
                c+=1
            j+=1
        print(ch,":",c)
    i+=1