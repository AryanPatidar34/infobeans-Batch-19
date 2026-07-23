'''
A
B B
C  C
D    D
EEEEEEEEE
'''

n=int(input("Enter the number"))
i=1
while i<=n:
    print()
    j=1
    while j<=2*i-1:
        if j==1 or j==2*i-1 or i==n:
            print(chr(64+i),end="")
        else:
            print(" ",end="")
        j+=1
        
   
    i+=1