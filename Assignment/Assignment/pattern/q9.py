''' 
    1
   10
  101
 1010
10101
'''


n=int(input("Enter the number"))
i=1
while i<=n:
    print()
    j=n-i
    while j>=1:
        print("#",end=" ")
        j-=1
    s=1
    while s<=i:
        if s%2!=0:
            print("1",end=" ")
        else:
            print("0",end=" ")
        s=s+1
    i=i+1