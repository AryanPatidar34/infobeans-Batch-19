'''
4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407'''

a=int(input("Enter the number"))
b=int(input("Enter the number"))

for n in range(a,b+1):
    if n>2 and n<10:
       continue
    else:
       temp=n
       l=len(str(n))
       sum=0
       for j in range(len(str(n))+1):
        d=n%10
        n=n//10
        sum=sum+d**l
    if sum==temp:
        print(temp)      
        