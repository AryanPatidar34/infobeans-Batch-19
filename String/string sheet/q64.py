'''
64Count frequency of each vowel.
 S = "programming" 
o: 1, a: 1 (e, i, u: 0)
'''
s=input("Enter the string")
vis=""
for i in s:
    if i in 'aeiou':
        if i not in vis:
            vis+=i
            c=s.count(i)
            print(i,":",c,end=",")