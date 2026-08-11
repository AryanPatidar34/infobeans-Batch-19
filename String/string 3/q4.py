'''
4.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop
'''

n=input("Enter your sentence : ")
final=""
rev=""
count=1
for ch in n:
     if ch!=' ':
         rev=rev+ch
     if ch==" " or count==len(n):
         if rev!=" ":
               final+=rev[::-1]+" "     
               rev=""
            
                 
     count+=1

print(final)
     

'''

#using while loop

n=input("Enter your message")+" "
rev=""
final=""
count=0
for ch in n:
    if ch==" "or count==len(n):
        if rev!=" ":
            i=-1
            while i>=-len(rev):
                ch=rev[i]
                final=final+ch
                i-=1
            final+=" "
            rev=""
    else:
        rev=rev+ch
       
    count+=1



print(final)
'''




