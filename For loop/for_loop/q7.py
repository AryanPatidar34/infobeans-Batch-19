'''
*7. Count Even Digits*
A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are even.
Write a program to *count the number of even digits in a given number using loops*.

Input: 123456
Output: Even digits count = 3
'''
#using for loop
'''
n= int(input("Enter the number"))
count =0
rev =0
for i in range(len(str(n))):
    rev = n%10
    if rev%2==0:
        count+=1
    n= n//10

print("Even digit count :"count)'''



#using while loop
n= int(input("Enter the number"))
count=0
rev=0
while n>0:
     rev=n%10
     if rev%2==0:
         count+=1
     n=n//10
print("Even digit count :",count)