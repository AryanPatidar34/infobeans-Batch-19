'''
A
BB
CCC
DDDD
EEEEE
'''
n=int(input("Enter the number"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        print(chr(64+i),end="")
        j+=1
    i+=1
