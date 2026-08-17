'''
ABCDE
ABCD
ABC
AB
A
'''
n=int(input("Enter the number"))
i=1
while i<=n:
    print()
    j=n
    s=1
    while j>=i:
        print(chr(64+s),end="")
        j-=1
        s+=1
    i+=1
