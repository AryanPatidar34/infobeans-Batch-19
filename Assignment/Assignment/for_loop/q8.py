'''
*8. Count Odd Digits*
A banking system flags IDs with too many odd digits for further verification.
Write a program to *count the number of odd digits in a given number using loops*.

Input: 123456
Output: Odd digits count = 3
'''

#using for loop
'''
n = int(input("Enter the number"))
rev = 0
count=0
for i in range(len(str(n))):
    rev = n%10
    if rev%2!=0:
        count+=1
    n=n//10
print("odd digits count :",count)'''



#using while loop

n = int(input("Enter the number"))
rev = 0
count=0
while n>0:
      rev = n%10
      if rev%2!=0:
          count+=1
      n=n//10
print('odd digits count :',count)
    