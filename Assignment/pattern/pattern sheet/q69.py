'''
     *********
      ******* 
       ***** 
        ***
         *
'''
n=int(input("Enter the number"))
i=n

while i>=1:
    print()
    s=1
    while s<n-(i-1):
        print(" ",end="")
        s+=1
    j=1
    while j<=2*i-1:
        print("*",end="")
        j+=1
       
    i-=1