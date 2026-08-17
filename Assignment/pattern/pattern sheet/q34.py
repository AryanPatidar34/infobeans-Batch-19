'''
EEEEE
DDDD
CCC
BB
A

'''
n=int(input("Enter the number"))
i=1
s=n
while i<=n:
    print()
    j=n
    
    while j>=i:
        print(chr(64+s),end="")
        j-=1
    s-=1
    i+=1