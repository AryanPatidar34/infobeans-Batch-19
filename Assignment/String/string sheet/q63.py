'''
63Count frequency of each character. 
S = "aabcc" 
a: 2, b: 1, c: 2
'''
s=input("Enter the string")
vis=""
for i in s:
    if i not in vis:
        vis+=i
        c=s.count(i)
        print(i,":",c,end=",")