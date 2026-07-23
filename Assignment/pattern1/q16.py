'''
a
bc
def
ghij
klmno
'''
n=int(input("Emter the number"))
i=1
k=1
while i<=n:
    print()
    j=1
    while j<=i:
        print(chr(96+k),end="")
        k+=1
        j+=1
    i+=1