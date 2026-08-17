'''
55555
4  4
3 3
22
1
'''
n=int(input("Enter the number"))
i=1
d=n
while i<=n:
    print()
    j=n
    while j>=i:
        if i==1 or j==n or j==i:
             print(d,end="") 
        else:
            print(" ",end="")
        j-=1
    d-=1
    i+=1
    