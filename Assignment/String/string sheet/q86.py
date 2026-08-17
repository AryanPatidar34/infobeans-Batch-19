'''
86
Print all permutations of a string without repetition.
 S = "ab"
 "ab",
 "ba"
'''
s=input("Enter string")
for i in range(len(s)):
    ch=s[i]
    cs=ch
    temp=""
    for j in range(1,len(s)):
        cs=cs+s[j]
        for k in range(len(cs),len(s)):
            if s[k] not in temp:
                temp+=s[k]
        print(cs+temp)
        
        
    
    


