'''
n=6
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4
'''

n=int(input("Enter the number"))
i=1
while i<=n:
    print()
    j=0
    while j<i:
        print(j, end=" ")
        j=j+1
    s=n-i
    while s>=1:
        print("#",end=" ")
        s-=1
    i=i+1

