'''
5.
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code
'''

n=input("Enter String").lower()
temp=n
i=-1
rev=""
while i>=-len(n):
   ch=n[i]
   rev=rev+ch
   i-=1

if temp==rev:
     print("palindrome")
else:
    print("not palindrome")
    