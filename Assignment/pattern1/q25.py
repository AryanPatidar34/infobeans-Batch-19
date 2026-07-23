'''
5
54
543
5432
54321
'''

n=int(input("Enter the number"))
i=1
while i<=n:
    print()
    j=n
    while j>n-i:
        print(j,end="")
        j-=1
    s=n-1
    while s>=i:
        print(" ",end="")
        s-=1
    i=i+1
        


