'''
123456
54321
1234
321
12
1
'''
n=int(input("Enter the number"))
i=1
t=n
while i<=n:
    print()
    j=n
    s=1
    while j>=i:
          if i%2!=0:
             print(s,end="")
             s+=1
             j-=1
          else:
              j=t
              while j>=1:
                 print(j,end="")
                 j-=1
              
              
                                 
       
    t-=1 
    i+=1
