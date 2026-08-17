'''
     x
     xx
     xxx
     xxxx
     xxx
     xx
     x
'''
n=int(input("Enter the number"))
i=n

while i>=1:
    print()
    j=n
    while j>=i:
              if i<n//2+1:
                   k=n-i+1
                   while k>=1:
                       print("x",end="")
                       k-=1
              else:
         
                  print("x",end="")
                
             
              j-=1
 
    i-=1
    
