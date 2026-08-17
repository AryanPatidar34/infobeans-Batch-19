'''
79
Divide a string into n equal parts. 
S = "abcdef", n = 3
 "ab", "cd", "ef"
'''

s=input("Enter string")
n=int(input("Enter parts"))
b=len(s)//n
k=0

for i in range(n):
     temp=""
     for j in range(b):
        temp=temp+s[k]
        k+=1
     print(temp,end=" ")
        
    
        
    
        
    
    