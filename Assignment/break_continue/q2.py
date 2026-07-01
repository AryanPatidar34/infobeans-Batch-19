'''
2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4'''

m = int(input("Enter the number"))
n = int(input("Enter the number"))
count=0
'''
for i in range(m,n+1):
    if i%7==0:
        count=count+1
    else:
        continue
print(count)'''


#using while loop
while m<=n:
     m=m+1
     if m%7==0:
         count=count+1
     else:
         continue
print("count :",count)
