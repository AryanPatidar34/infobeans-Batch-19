'''
Remove occurrences of a word. 
S = "a test b test c", 
Word = "test",
 Remove All "a b c"
'''
s=input("Enter the string")
n=s.split()
i=0
while i<len(n):
    ch=n[i]
    c=n.count(ch)
    if c>1:
        pass
    else:
        print(ch,end=" ")
    i+=1
