'''
4.
Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]
'''

n=int(input("Enter the size"))
a=[]
for i in range(n):
    t=int(input("Enter elements : "))
    a.append(t)
print(a)
palindrome=[]
c=0
lar=0
for x in a:
    temp=x
    rev=0
    while x>0:
        d=x%10
        rev=rev*10+d
        x=x//10
    if temp==rev:
        palindrome.append(temp)
        if temp>lar:
            lar=temp
        c+=1

print("Palindrome :",palindrome)
print("Count :",c)
print("Largest:",lar)
palindrome.sort()
print("Sorted :",palindrome)
