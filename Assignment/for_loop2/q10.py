'''
10. Student ID Validity Checker (Count Odd Digits)
A school management system assigns numeric IDs to students. The administration wants to verify IDs by checking how many odd digits are present in each ID number. IDs with more odd digits are sent for manual review.

Write a program to count the number of odd digits in a given student ID using loops.

Input:
572943

Output:
Odd Digits Count = 3'''


n = int(input("Enter the number"))
'''
count=0
while(n>0):
      d = n%10
      if d%2!=0:
          count=count+1
      n=n//10

print(count)'''

count=0
l =len(str(n))
for i in range(l,0,-1):
    d=n%10
    if d%2!=0:
        count=count+1
    n=n//10

print(count)


