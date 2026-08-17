'''
ABCDE
A  D
A C
AB
A
'''
n=int(input("Enter the number"))
i=1

while i<=n:
    print()
    j=n
    s=1
    while j>=i:
           if  i==1 or j==n or j==i:
               print(chr(64+s),end="")
               
           else:
               print(" ",end="")
           s+=1
           j-=1
    i+=1
  