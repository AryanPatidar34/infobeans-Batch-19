'''
3. First Digit of Number
A university receives thousands of application IDs. The first digit of each ID represents the department code, so the admission software must read the first digit quickly.
Write a program to find the first digit of a number using loops.

Input:
53892

Output:
First Digit = 5 '''
'''
n=int(input("Enter the number"))
rev =""
while n>0:
     d = n%10
     rev += str(d)
     n=n//10
 
rev = int(rev)
d1 = rev%10
print("First digit :",d1)'''



'''
n=int(input("Enter the number"))
l =len(str(n))
for i in range(l-1):
        n=n//10
print(n)
'''

n=int(input("Enter the number"))
s = str(n)
for i in s:
    
    print(i)