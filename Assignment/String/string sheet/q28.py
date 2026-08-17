'''
Count occurrences of a word. 
S = "word word other word", 
Word = "word" 3
'''
s=input("Enter the string")
word=input("Enter the word")
n=s.split()
i=0
c=0
while i<len(n):
    ch=n[i]
    if ch==word:
        c+=1
    i+=1
print(c)