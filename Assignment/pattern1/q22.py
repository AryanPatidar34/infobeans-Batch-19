'''
A
AB
A C
A  D
ABCDE
'''
n=int(input("Enter the number"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if j==1 or j==i or i==n:
            print(chr(64+j),end="")
        else:
            print(" ",end="")
        j+=1
    i+=1