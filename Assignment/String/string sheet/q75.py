'''
75Find the longest common prefix among strings.
 Strings = ["flower", "flow", "flight"]
 "fl"
'''
n=input("Enter string ").split()
s=n[0]
i=1
temp=""
temp1=""
while i<len(n):
    c=n[i]
    j=0
    while j<len(s) and j<len(c):
        if i==1:
             if s[j]==c[j]:        
                temp1+=s[j]
         
             else:
                 break
        else:
            k=0
            temp1=""
            while k<len(temp) and k<len(c):
                 if temp[k]==c[k]:              
                     temp1+=temp[k]
                 
                      
                 else:
                     break
            
                 k+=1
        temp=temp1

        j+=1  
    i+=1


print(temp)
