'''
74Find the longest substring without repeating characters. S = "abcabcbb" "abc"
'''
s=input("Enter string")
lar=""
for i in range(len(s)):
    ch=s[i]
    cs=ch
    
    res=""
    for j in range(i+1,len(s)):
          ch1=s[j]
          if ch1 not in cs:
                cs+=ch1
          else:
              break
          if len(cs)>len(lar):       
               lar=cs
print(lar)   
                  
         