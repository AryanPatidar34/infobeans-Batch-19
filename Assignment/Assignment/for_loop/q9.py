'''
*9. Check All Digits Are Even*
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to *check whether all digits of a number are even using loops*.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even
'''
#using for loop 
'''
n=int(input("Enter the number"))
count=0
evendigit=0
for i in range(len(str(n))):
    rev =0
    count+=1
    rev = n%10
    if rev%2==0:
        evendigit+=1
    n=n//10

if count==evendigit:
    print("All even digit")
else:
    print("not all even")'''

#using while loop
n=int(input("Enter the number"))
count=0
evendigit=0

while n>0:
      rev=0
      count+=1
      rev=n%10
      if rev%2==0:
          evendigit+=1
      n=n//10

if count==evendigit:
    print("All even digit")
else:
    print("not all even")

    
    
