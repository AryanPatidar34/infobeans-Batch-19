'''
80Print list items containing all characters of a given word.
 List = ["apple", "plea"], Word = "pal" 
output:
"apple", "plea"
'''
s=input("Enter string").split()
word=input("Enter string")
for i in range(len(s)):
     ch=s[i]
     for j in range(len(word)):
         cs=word[j]
         if cs in ch:
             pass
         else:
             break
    
     else:
          print(ch)    
        
         

