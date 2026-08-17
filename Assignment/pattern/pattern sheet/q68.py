'''
      #
     *#* 
    **#** 
   ***#*** 
  ****#****
'''
n=int(input("Enter the number"))
i=1
while i<=n:
    print()
    s=n-1
    while s>=i:
        print(" ",end="")
        s-=1
    j=1
    while j<=2*i-1:
       if j==i:
           print("#",end="")
       else:
           print("*",end="")
       j+=1
    i+=1