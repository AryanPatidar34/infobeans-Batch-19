'''
1
123
12345
1234567
123456789
'''
n=int(input("Enter the number"))
i=1
s=1
while i<=n:
    print()
    j=1
    s=1
    while j<=i*2-1:
        print(s,end="")
        j+=1
        s+=1
    i+=1