'''
5. Palindrome Check
A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to *check whether a given number is a palindrome using loops*.

Input: 121
Output: Palindrome
'''

#using for loop
'''
n = int(input("Enter the number"))
temp=n
rev =0
for i in range(len(str(n))):
    rev=rev*10+n%10
    n = n//10

if rev==temp:
    print("palindrome")
else:
    print("not palindrome")
'''
   
#using while loop
n = int(input("Enter the number"))
rev=0
temp=n
while n>0:
     rev = rev*10+n%10
     n = n//10

if temp==rev:
   print("palindome")

else:
   print('not palindrome')