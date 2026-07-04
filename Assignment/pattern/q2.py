'''
WAP to print Square ,Cube and Square Root of all numbers from 1 to N
'''

import math
n=int(input("Enter the number"))
for i in range(1,n+1):
    sq=i**2
    cb=i**3
    sqr=math.sqrt(i)
    print(i)
    print("Square:",sq)
    print("Cube:",cb)
    print("Sq root:",sqr)
    print()
    
        

