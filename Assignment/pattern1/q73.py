'''
   5 5 5 5 5
    4 4 4 4
     3 3 3
      2 2
       1
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
    
    while j<=i:
        print(i,end=" ")
        j+=1
            
    
    i-=1

