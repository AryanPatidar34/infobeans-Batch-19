'''
2.
Fibonacci Series Generator

A learning app helps students understand number patterns. One of the most important patterns is the Fibonacci series, where each number is the sum of the previous two numbers.

The series starts with:
0 1

Write a program to:

- Read a number n (number of terms)
- Print the Fibonacci series up to n terms using a loop

Input:
7

Output:
0 1 1 2 3 5 8
'''


n=int(input("Enter the number"))
for i in range(0,2):
    if i==0:
        print(i,end=" ")
    if i==1:
        print(i,end=" ")
        sl=i
i=1
while i<=n-2:
    if i==1:
        print(i,end=" ")
        l=i
    if i>1:
        sum=l+sl
        print(sum,end=" ")
        sl=l
        l=sum
    i=i+1
        
                     
    
        
        
            
                        
        