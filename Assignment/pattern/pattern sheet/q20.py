'''
1
12
1 3
1  4
12345
'''

n=int(input("Enter the number"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if i==n or i==j or j==1:
            print(j,end="")
            
        else:
            print(" ",end="")
        j+=1
    i+=1
    