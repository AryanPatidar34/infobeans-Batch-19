'''
*****
*  *
* *
**
*
'''
n=int(input("Enter the number"))
i=1

while i<=n:
    print()
    j=n
    while j>=i:
            
      if i==1 or  j==n  or j==i :
          print("*",end="")
      else:
          print(" ",end="")
      j-=1
    
    i+=1