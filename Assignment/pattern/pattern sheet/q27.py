'''
1
10
1 1
1  0
10101
'''
n=int(input("Enter the number"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if j%2==0:
            print("0",end="")
        else:
            print("1",end="")
        j+=1
    i+=1