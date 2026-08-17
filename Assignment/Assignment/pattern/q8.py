'''
n=6
654321
 65432
  6543
   654
    65
'''

n=int(input("Enter the number")) 
i=1
while i<=n:
    print()
    s=1
    while s<i:
        print("#",end=" ")
        s=s+1
    j=6
    while j>=i:
        print(j,end=" ")
        j=j-1
            
    i=i+1
    