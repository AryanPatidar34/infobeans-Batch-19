'''
a
bc
d f
g  j
klmno
'''

n=int(input("Enter the number"))
i=1
k=1
while i<=n:
    print()
    j=1
    while j<=i:
        if j==1 or i==j or i==n:
            print(chr(k+96),end="")
        else:
            print(" ",end="")
        k+=1
        j+=1
    i+=1