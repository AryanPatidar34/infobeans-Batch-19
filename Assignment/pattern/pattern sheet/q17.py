'''
*
##
***
####
*****
'''
'''
n=int(input("Enter the number"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
       if i%2!=0:
          print("*",end="")
       else:
        print("#",end="")
       j+=1

    i+=1
'''

s=input("Enter the strnig")
i=len(s)-1
while i>=0:
    print(s[i])
    i-=1