'''
55555
4444
333
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
        print(d,end="")
        j-=1
    d-=1   
    i+=1