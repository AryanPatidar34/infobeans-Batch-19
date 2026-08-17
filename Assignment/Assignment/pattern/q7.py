'''
n=6
     *     #####
    **     ####
   ***     ###
  ****     ##
 *****     #
******
'''

n=int(input("Enter the number"))
i=1
while i<=n:
    print()
    j=1
    while j<=n-i:
        print(" ",end=" ")
        j=j+1        
    s=1
    while s<=i:
        print("*",end=" ")
        s=s+1
    i=i+1