'''
3.  Smart Chat Message Cleaner

A social media company noticed that users often enter messages with
unnecessary spaces. To improve readability and storage efficiency, the
system should remove extra spaces and keep only a single space between
words.

Input: Enter message: Java is easy

Output: Cleaned Message: Java is easy
'''
n=input("Enter the number")
s=''
i=0
while i<len(n):
    ch=n[i]
    if ch!=" ":
        while i<len(n):
            ch=n[i]
            if n[i]==" " and n[i-1]==" ":
                s=s
            else:
                s=s+ch
            i=i+1
    i+=1
  
print(s)                    
                       

   