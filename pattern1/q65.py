'''
        1
      1 1
    1 2 1
  1 3 3 1
1 4 6 4 1
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
    while j<=i:
        if j==1 or j==i:
            print("1",end="")
            
        else:
            if i%2==0:
                print(i-1,end="")
            else:
                if j%2==0:
                    print(i-1,end="")
                else:
                    print((i-2)*2,end="")                              
                    
        j+=1
    i+=1