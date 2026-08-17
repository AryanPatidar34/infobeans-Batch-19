
'''
1
01
101
0101
10101
'''
n=int(input("Enter the number"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
            if i%2==0:
                if j%2!=0:
                    print("0",end="")
                else:
                     print("1",end="")
            else:
                 if j%2==0:
                      print("0",end="")
                 else:
                      print("1",end="")
           
        
            j+=1      
            
    i+=1