'''
3. Multiplication Table
A shopkeeper wants to calculate bulk pricing for a product. If one item costs ₹n, then cost for multiple quantities can be calculated using multiplication.
Write a program to print the *multiplication table of a given number up to 10 using loops*.

Input: n = 6
Output:
6 x 1 = 6
6 x 2 = 12
...
6 x 10 = 60
'''
#using for loop
'''
n = int(input("Enter the number"))
res=1
for i in range(1,11):
    res=n*i
    print(n,"*",i,"=",res)'''
    


#using while loop
n = int(input("Enter the number"))
i=1
res =1
while i<=10:
    res=n*i
    print(n,"*",i,'=',res)
    i+=1
      
