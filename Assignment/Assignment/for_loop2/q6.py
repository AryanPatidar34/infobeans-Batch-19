'''
6. Sum of Factors
A puzzle-based game rewards users based on the sum of all factors of a chosen number. The system calculates the total score using all factors of the entered number.
Write a program to find sum of factors using loops.

Input:
6

Output:
Sum = 12'''


'''
n = int(input("Enter the number"))
sum=0
for i in range(1,n+1):
    if n%i==0:
        sum = sum+i 

print("sum is:",sum)'''


#using while loop
n = int(input("Enter the number"))
sum=0
i=1
while n>=i:
     if n%i==0:
         sum=sum+i
     i=i+1
print(sum)