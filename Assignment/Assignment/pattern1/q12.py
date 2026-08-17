'''
a
ab
abc
abcd
abcde
'''
n=int(input("Enter the number"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        print(chr(96+j),end="")
        j+=1
    i+=1